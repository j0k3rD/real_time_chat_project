from pybreaker import CircuitBreaker
from decouple import config
import requests

class Functions:

    __userBreaker = CircuitBreaker(fail_max=5, reset_timeout=60)

    def __init__(self, CircuitBreaker):
        self.__userBreaker = CircuitBreaker

    @__userBreaker
    def get_token(self):
        """
        Función que obtiene el token de la API de chat.
        """
        params = {"username": config('USERNAME_DATA'), "password": config('PASSW_DATA')}
        params_response = requests.post("http://chatservice:7000/api/token/", data=params) # TODO: cambiar por chat_url no funciona, de momento lo dejo hardcodeado.
        return params_response.json()
        