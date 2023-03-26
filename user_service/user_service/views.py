from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # la ruta de la plantilla de inicio de sesión
    redirect_authenticated_user = True  # redirecciona al usuario autenticado a la página principal
    extra_context = {'title': 'Inicio de sesión'}  # cualquier contexto adicional que desee agregar

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse("¡Bienvenido de nuevo, {}!".format(user.username))
            else:
                return HttpResponse("Nombre de usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})