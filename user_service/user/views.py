from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from user.models import User
from decouple import config
import redis, mysql
from django.http import JsonResponse
from user.models import User
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def user_login(request):
    user_url = config('USER_URL')
    if request.method == 'POST':
        # username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # user = User.objects.get(username=username)
        user = User.objects.get(email=email)
        checkpassword = check_password(password, user.password)
        print("Esto es passw: ", password)
        if user is not None:
            if checkpassword:
                return redirect(config('CHAT_URL') + "/menu/", {'user_url': user_url})
            else:
                return HttpResponse("Nombre de usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

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
    
# Vista para registrar usuarios en la pagina
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