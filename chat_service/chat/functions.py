from rest_framework_simplejwt.tokens import AccessToken
from django.http import HttpResponseRedirect
from decouple import config

# Autenticación del token, si no existe o es inválido, redirige al login
# TODO: Ver si se puede refrescar el token en caso de expirar.
def autenticate(token_str):

    if token_str is None:
        return False

    try:
        token = AccessToken(token_str)
    except:
        token = None

    if token is not None:
        return True
    else:
        return False
    
def get_access_token(request):
    return request.COOKIES.get('access_token', None)

def del_access_token(request):
    response = HttpResponseRedirect(config('USER_URL') + "/login/")
    response.delete_cookie('access_token')
    return response