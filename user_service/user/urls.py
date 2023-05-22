"""project_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import user_login, health_check, register, refresh_token, remove_token

urlpatterns = [
    path('login/', user_login, name='login'),
    path('health_check/', health_check, name='health_check'),
    path('register/', register, name='register'),
    path('api/refresh/', refresh_token, name='remove_token'),
    path('api/blacklist/', remove_token, name='refresh_token'),
    path('', user_login, name='login'),
]