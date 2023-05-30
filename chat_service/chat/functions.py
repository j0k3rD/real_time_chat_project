# from consulate import Consul
# from decouple import Config, RepositoryEnv
from rest_framework_simplejwt.tokens import AccessToken
import requests
# import json

# CONSUL_AGENT_HOST = '172.18.0.2'
# consul_client = Consul(host=CONSUL_AGENT_HOST)

# # Obtener valores de Consul para el chat_service
# config = Config(RepositoryEnv('.env'))

# Ejemplo de obtener la key LOCAL_USER_URL desde Consul
# local_user_url = consul_client.kv.get('chat_service/config/LOCAL_USER_URL')[1]['Value'].decode('utf-8')

# key = 'chat_service/config'
# index, data = consul_client.kv.get(key)

# if data:
#     value = data['Value'].decode('utf-8')
#     config_dict = json.loads(value)
#     local_user_url = config_dict.get('LOCAL_USER_URL')
#     print("LOCAL_USER_URL:", local_user_url)
# else:
#     print("La clave 'LOCAL_USER_URL' no existe en Consul.")

# Autenticación del token, si no existe o es inválido, redirige al login
# TODO: Ver si se puede refrescar el token en caso de expirar.
def authenticate(token_str):
    if token_str is None:
        return None

    try:
        token = AccessToken(token_str)
    except:
        token = None
    return token

def refresh_token(refresh_token):
    response = requests.post(f'{local_user_url}/api/refresh/', data={'refresh_token': refresh_token})
    return response

def blacklist_refresh_token(refresh_token):
    response = requests.post(f'{local_user_url}/api/blacklist/', data={'refresh_token': refresh_token})
    return response
    
def get_access_token(request):
    return request.COOKIES.get('access_token', None)

def set_access_token(response, token):
    response.set_cookie('access_token', token)
    return response

def del_access_token(response):
    response.delete_cookie('access_token')
    return response

def get_refresh_token(request):
    return request.COOKIES.get('refresh_token', None)

def set_refresh_token(response, refresh_token):
    response.set_cookie('refresh_token', refresh_token)
    return response

def del_refresh_token(response):
    response.delete_cookie('refresh_token')
    return response