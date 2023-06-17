import redis
import mysql.connector
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from decouple import config
import pybreaker
from chat.services.circuit_breaker import ChatListener
from . import functions
from .services.group_service import GroupService
from .services.message_service import MessageService
from consulate import Consul


chatBreaker = pybreaker.CircuitBreaker(fail_max=5, reset_timeout=60, listeners=[ChatListener()])
groupService = GroupService()
messageService = MessageService()

consul_client = Consul(host='consul')
kv = consul_client.kv

@chatBreaker
def logout(request):
    if request.method == 'POST':
        # Redirigir a la página de login
        response = HttpResponseRedirect(kv['chatservice/config/USER_URL'] + "/login/")
        functions.del_refresh_token(response)
        functions.del_access_token(response)
        return response

@chatBreaker
def get_token_page(request):
    refresh = request.GET.get('refresh', None)

    if refresh is not None:
        token = functions.refresh_token(refresh)
        access_token = token.json()['access_token']
        refresh = token.json()['refresh']

        response = HttpResponseRedirect("/menu/")
        print(type(response))
        response = functions.set_access_token(response, access_token)
        response = functions.set_refresh_token(response, refresh)
        return response

@chatBreaker
def get_main_page(request):
    user_url = kv['chatservice/config/USER_URL']
    chat_url = kv['chatservice/config/CHAT_URL']
    token = functions.authenticate(functions.get_access_token(request))
    if token is not None:
        context = {
            'groups': groupService.get_all(),
            'chat_url': chat_url,
            'user_id': token['user_id'],
            'username': token['username'],
            'email': token['email'],
        }
        return render(request, 'chat_main_page.html', context)
        # return HttpResponse("Esto es el menu")
    else:
        return HttpResponseRedirect(user_url + "/login/", {'error': 'Invalid token.'})

@chatBreaker
def get_group_chat(request, group_id):
    user_url = kv['chatservice/config/USER_URL']
    chat_url = kv['chatservice/config/CHAT_URL']
    token = functions.authenticate(functions.get_access_token(request))
    if token is not None:
        group = groupService.get_by_id(group_id)
        messages = messageService.get_by_group_id_order_by_date(groupModel = group)

        context = {
            'groups': groupService.get_all(),
            'group': group,
            'chats': messages,
            'chat_url': chat_url,
            'user_id': token['user_id'],
            'username': token['username'],
            'email': token['email'],
            'current_user': request.user,
        }

        return render(request, 'group_chat.html', context)
    else:
        return HttpResponseRedirect(user_url + "/login/", {'error': 'Invalid token.'})

@chatBreaker
def get_group(request, group_id):
    user_url = kv['chatservice/config/USER_URL']
    chat_url = kv['chatservice/config/CHAT_URL']
    token = functions.authenticate(functions.get_access_token(request))
    if token is not None:
        group = groupService.get_by_id(group_id)
        messages = messageService.get_by_group_id_order_by_date(groupModel = group)

        context = {
            'group': group,
            'chats': messages,
            'chat_url': chat_url,
            'user_id': token['user_id'],
            'username': token['username'],
            'email': token['email'],
        }

        return render(request, 'group.html', context)
    else:
        return HttpResponseRedirect(user_url + "/login/", {'error': 'Invalid token.'})

def health_check(request):
    '''
    Función que chequea el estado de la base de datos y el servidor de redis
    '''
    #Checkemos el Redis
    redis_host = kv['chatservice/config/REDIS_HOST']
    redis_port = kv['chatservice/config/REDIS_PORT']

    try:
        r = redis.Redis(host=redis_host, port=redis_port, socket_connect_timeout=1, socket_timeout=1)
        r.ping()
        redis_status = 200
    except redis.exceptions.ConnectionError:
        redis_status = 500

    #Checkemos MySQL
    mysql_host = kv['chatservice/config/DATABASE_HOST']
    mysql_port = kv['chatservice/config/DATABASE_PORT']
    mysql_user = kv['chatservice/config/DATABASE_USER']
    mysql_password = kv['chatservice/config/DATABASE_PASSWORD']
    mysql_database = kv['chatservice/config/DATABASE_NAME']

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