from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # la ruta de la plantilla de inicio de sesión
    redirect_authenticated_user = True  # redirecciona al usuario autenticado a la página principal
    extra_context = {'title': 'Inicio de sesión'}  # cualquier contexto adicional que desee agregar

