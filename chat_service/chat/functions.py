from rest_framework_simplejwt.tokens import AccessToken
import requests
from consulate import Consul


consul_client = Consul(host='consul')
kv = consul_client.kv

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

def get_url():
    user_url = kv['chatservice/config/USER_URL']
    return user_url

def refresh_token(refresh_token):
    response = requests.post(f'{get_url()}/api/refresh/', data={'refresh_token': refresh_token}, verify=False)
    return response

def blacklist_refresh_token(refresh_token):
    response = requests.post(f'{get_url()}/api/blacklist/', data={'refresh_token': refresh_token}, verify=False)
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