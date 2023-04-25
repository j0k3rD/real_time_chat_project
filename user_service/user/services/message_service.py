from ..repositories.message_repository import MessageRepository
from ..services.services import Service

repository = MessageRepository()

class MessageService(Service):
    '''
    Clase que representa el servicio de la entidad Message
    param:
        - Service: Clase que hereda de la interfaz Service
    '''

    def add(self, model):
        return repository.create(model)
        
    def get_all(self):
        return repository.find_all()

    def get_by_id(self, id):
        return repository.find_by_id(id = id)