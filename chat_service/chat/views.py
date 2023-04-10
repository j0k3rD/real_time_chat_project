import redis
import mysql.connector
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from chat.models import Message, Group
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from decouple import config


# @login_required
def group_chat(request, group_id):
    group = Group.objects.get(id=group_id)
    messages = Message.objects.filter(group=group).order_by('date')

    
    context = {
        'group': group,
        'messages': messages,
    }

    return render(request, 'group.html', context)

# @login_required
def chat_main_page(request):
    groups = Group.objects.all()
    context = {
        'groups': groups,
    }
    return render(request, 'chat_main_page.html', context)

# @login_required
# def send_message(request):
#     if request.method == 'POST':
#         content = request.POST.get('content')
#         group_id = request.POST.get('group_id')
#         sender = request.user
#         group = Group.objects.get(id=group_id)
#         message = Message.objects.create(group=group, sender=sender, content=content)
#         data = {'success': True}
#         return JsonResponse(data)
#     else:
#         data = {'success': False}
#         return JsonResponse(data)

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