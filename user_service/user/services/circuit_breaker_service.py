# Aplicamos patron circuit breaker para evitar que el servicio se caiga

from pycircuitbreaker import circuit
from user.services import UserService

@circuit(failure_threshold=3, expected_exception=Exception)
def get_login(request):
    return UserService.get_login(request)