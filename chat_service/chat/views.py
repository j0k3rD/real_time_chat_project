import redis
import mysql.connector
from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from chat.models import Message, Group
from django.http import HttpResponse, HttpResponseRedirect
from decouple import config


def get_main_page(request):
    user_url = config('USER_URL')
    access_token = get_access(request)
    if access_token is not None:
        groups = Group.objects.all()
        context = {
            'groups': groups,
        }
        return render(request, 'chat_main_page.html', context)
        # return HttpResponse("Esto es el menu")
    else:
        return HttpResponseRedirect(user_url + "/login/")

def get_group(request, group_id):
    user_url = config('USER_URL')
    access_token = get_access(request)
    if access_token is not None:
        group = Group.objects.get(id=group_id)
        messages = Message.objects.filter(group=group).order_by('date')

        
        context = {
            'group': group,
            'messages': messages,
        }

        return render(request, 'group.html', context)
    else:
        return HttpResponseRedirect(user_url + "/login/")

def get_access(request):
    access_token = request.COOKIES.get('access_token')
    return access_token


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