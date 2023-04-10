from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from user.models import User
from decouple import config

# Create your views here.

def user_login(request):
    static_path = config('STATIC_PATH')
    style_path = config('STYLES_PATH')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = User.objects.get(username=username)
        print(user)
        print(user.username, user.password)
        if user is not None:
            print("user is not None")
            if user.password == password:
                return redirect(config('CHAT_URL'))
            else:
                return HttpResponse("Nombre de usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})