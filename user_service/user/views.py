from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from user.models import User
from decouple import config
import redis, mysql
from django.http import JsonResponse
from user.models import User
from django.contrib.auth.hashers import make_password, check_password
import requests as r
import pybreaker
from user.services.circuit_breaker import UserListener

user_breaker = pybreaker.CircuitBreaker(fail_max=5, reset_timeout=60, listeners=[UserListener()])

@user_breaker
def get_token():
    # Obtengo el token accediendo con admin
    params = {"username": config('USERNAME_DATA'), "password": config('PASSW_DATA')}
    params_response = r.post("http://chatservice:7000/api/token/", data=params) # TODO: cambiar por chat_url no funciona, de momento lo dejo hardcodeado.
    return params_response.json()

@user_breaker
def user_login(request):
    user_url = config('USER_URL')
    chat_url = config('CHAT_URL')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.get(email=email)
        #! Este chequeo va aca o en el servicio?
        checkpassword = check_password(password, user.password)
        if user is not None:
            if checkpassword:
                # En caso de devolver un true, obtengo el token y redirijo al usuario a la página de chat
                token = get_token()
                response = HttpResponseRedirect(chat_url + "/token/" + "?token={}".format(token["access"]), {'user_url': user_url})
                return response
                    
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# @user_login.error_handler
# def user_login_error_handler(cb, exc):
#     """
#     Handler for circuit breaker errors in user_login view.
#     """
#     # si se produce una excepción de circuit breaker, redirige al usuario a una página de error
           

@user_breaker
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Verifico que no esten vacios
        if username and email and password:
            # Compruebo si el email ya existe
            if User.objects.filter(email=email).exists():
                return render(request, 'register.html', {'error': 'El email ya existe.'})
            else:
                user = User(username=username, email=email)
                user.password = make_password(password)
                user.save()
                return redirect(config('USER_URL') + "/login/")
        else:
            return render(request, 'register.html', {'error': 'Todos los campos son obligatorios.'})
    else:
        return render(request, 'register.html')

def health_check(request):
    '''
    Función que chequea el estado de la db MySQL
    '''
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
        'mysql': mysql_status,
    }
    
    if all(value == 200 for value in data.values()):
        return JsonResponse(data, status=200)
    else:
        return JsonResponse(data, status=500)