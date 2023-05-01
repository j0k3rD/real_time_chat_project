from rest_framework_simplejwt.tokens import AccessToken

class Functions:
    # Autenticación del token, si no existe o es inválido, redirige al login
    # TODO: Ver si se puede refrescar el token en caso de expirar.
    def autenticate(self, token_str):
        try:
            token = AccessToken(token_str)
        except:
            token = None  
        return token
        
    def get_access_token(self, request):
        return request.COOKIES.get('access_token', None)

    def set_access_token(self, response, token):
        response.set_cookie('access_token', token)
        return response

    def del_access_token(self, response):
        response.delete_cookie('access_token')
        return response