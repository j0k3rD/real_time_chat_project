import redis
import mysql.connector
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from chat.models import Message, Group
from chat.functions import autenticate, get_access_token, del_access_token
from django.http import HttpResponseRedirect
from decouple import config
import pybreaker
from chat.services.circuit_breaker import ChatListener, LogListener

chat_breaker = pybreaker.CircuitBreaker(listeners=[ChatListener(), LogListener()])

@chat_breaker
def get_token_page(request):
    token = request.GET.get('token', None)
    user_url = config('USER_URL')

    if token is not None:
        response = HttpResponseRedirect("/menu/")
        response.set_cookie('access_token', token)
        return response
    else:
        return HttpResponseRedirect(user_url + "/login/")

@chat_breaker
def get_main_page(request):
    if request.method == 'POST':
        return del_access_token(request)
    else:
        user_url = config('USER_URL')
        chat_url = config('CHAT_URL')
        if autenticate(get_access_token(request)):
            groups = Group.objects.all()
            context = {
                'groups': groups,
                'chat_url': chat_url,
            }
            request
            return render(request, 'chat_main_page.html', context)
            # return HttpResponse("Esto es el menu")
        else:
            return HttpResponseRedirect(user_url + "/login/")

@chat_breaker
def get_group(request, group_id):
    user_url = config('USER_URL')
    chat_url = config('CHAT_URL')
    if autenticate(get_access_token(request)):
        group = Group.objects.get(id=group_id)
        messages = Message.objects.filter(group=group).order_by('date')

        context = {
            'group': group,
            'messages': messages,
            'chat_url': chat_url,
        }

        return render(request, 'group.html', context)
    else:
        return HttpResponseRedirect(user_url + "/login/")

def health_check(request):
    '''
    Función que chequea el estado de la base de datos y el servidor de redis
    '''
    #Checkemos el Redis
    redis_host = config('REDIS_HOST')
    redis_port = config('REDIS_PORT')

    try:
        r = redis.Redis(host=redis_host, port=redis_port, socket_connect_timeout=1, socket_timeout=1)
        r.ping()
        redis_status = 200
    except redis.exceptions.ConnectionError:
        redis_status = 500

    #Checkemos MySQL
    mysql_host = config('DATABASE_HOST')
    mysql_port = config('DATABASE_PORT')
    mysql_user = config('DATABASE_USER')
    mysql_password = config('DATABASE_PASSWORD')
    mysql_database = config('DATABASE_NAME')
    try:
        cnx = mysql.connector.connect(user=mysql_user, password=mysql_password, host=mysql_host, port=mysql_port, database=mysql_database)
        cnx.ping(True)
        mysql_status = 200
    except mysql.connector.Error as err:
        mysql_status = 500
    
    data = {
        'redis': redis_status,
        'mysql': mysql_status,
    }
    
    if all(value == 200 for value in data.values()):
        return JsonResponse(data, status=200)
    else:
        return JsonResponse(data, status=500)