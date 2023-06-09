"""
Django settings for chat_service project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import datetime
from consulate import Consul
from consulate.models import agent
import socket
# Set the project root directory
# PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# django settings module
# SETTINGS_MODULE = kv['DJANGO_SETTINGS_MODULE')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

consul_client = Consul(host='consul')
addr = socket.gethostbyname(socket.gethostname())
kv = consul_client.kv

#Check service
checks = agent.Check(
    name='Chat Service Check',
    http='https://chat.chat.localhost/health_check/',
    interval='10s',
    tls_skip_verify=True, #* Para que no verifique el certificado
    timeout="1s",
    status="passing"
)

# Register service
#* AGREGAR POLITICAS DE SEGURIDAD

consul_client.agent.service.register(
    name='chatservice',
    service_id = f'{kv["chatservice/config/NAME"]}-{addr}',  #Se agrega para que tome las diferentes instancias, ver id unico.
    address=addr, #* Nombre del container
    tags=[  
            "traefik.enable=true",
            "traefik.http.routers.chatservice.rule=Host(`chat.chat.localhost`)",# && PathPrefix(`/ws`)"
            "traefik.http.routers.chatservice.tls=true",
            "traefik.http.services.chatservice.loadbalancer.server.port=7000",
            "traefik.http.routers.chatservice.entrypoints=http,https,redis,mysql,wss",
            "traefik.http.services.chatservice.loadbalancer.sticky.cookie=true",
            "traefik.http.middlewares.chatservice-cb.circuitbreaker.expression=ResponseCodeRatio(500, 600, 0, 600) > 0.10 || NetworkErrorRatio() > 0.10 || LatencyAtQuantileMS(50.0) > 100"
        ],
    check=checks
    )

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = kv['SECRET_KEY')
SECRET_KEY = kv['chatservice/config/SECRET_KEY']
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.getenv('DEBUG')
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'chat',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'rest_framework',
    'rest_framework_simplejwt',
    # 'ConsulService',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'chat_service.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'frontend/build'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
            ],
        },
    },
]

ASGI_APPLICATION = 'chat_service.asgi.application'

WSGI_APPLICATION = 'chat_service.wsgi.application'

#! Consul configuration CON DJANGO-CONSUL (DEPRECATED)
# CONSUL_AGENT_ADDRESS = kv['CONSUL_AGENT_ADDRESS')
# CONSUL_AGENT_PORT = kv['CONSUL_AGENT_PORT')
# CONSUL_CHECK_URL = kv['CONSUL_CHECK_URL')
# CONSUL_CHECK_INTERVAL = kv['CONSUL_CHECK_INTERVAL')
# CONSUL_SERVICE_NAME = kv['CONSUL_SERVICE_NAME')
# CONSUL_SERVICE_ADDRESS = kv['CONSUL_SERVICE_ADDRESS')
# CONSUL_SERVICE_PORT = kv['CONSUL_SERVICE_PORT')



# INFORMATION FOR CONSUL REGISTRATION

# CONSUL_AGENT_ADDRESS Consul agent server's address

# CONSUL_AGENT_PORT Consul agent server's port

# CONSUL_CHECK_URL API on service used by consul server to check it's status

# CONSUL_CHECK_INTERVAL Status check interval

# CONSUL_SERVICE_NAME Local service name

# CONSUL_SERVICE_ADDRESS Local service address

# SERVICE_PORT Local service port


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': kv['chatservice/config/DATABASE_NAME'],
        'USER': kv['chatservice/config/DATABASE_USER'],
        'PASSWORD': kv['chatservice/config/DATABASE_PASSWORD'],
        'HOST': kv['chatservice/config/DATABASE_HOST'],
        'PORT': kv['chatservice/config/DATABASE_PORT'],
    },
}

# Cache and Channels, para el manejo de los sockets
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(kv['chatservice/config/REDIS_HOST'], kv['chatservice/config/REDIS_PORT'])],
        },
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


STATIC_URL = 'chatservice/config/STATIC_PATH/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/build/static'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'