#Aplicamos patron circuit breaker para evitar que el servicio se caiga

from circuitbreaker import circuit

from chat.services import ChatService

@circuit(failure_threshold=3, expected_exception=Exception)
def get_main_page(request):
    return ChatService.get_main_page(request)

@circuit(failure_threshold=3, expected_exception=Exception)
def get_group(request, group_id):
    return ChatService.get_group(request, group_id)

@circuit(failure_threshold=3, expected_exception=Exception)
def get_access(request):
    return ChatService.get_access(request)

@circuit(failure_threshold=3, expected_exception=Exception)
def health_check(request):
    return ChatService.health_check(request)