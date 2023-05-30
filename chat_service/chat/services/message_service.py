from ..repositories.message_repository import MessageRepository
from .services import Service
from ..models import Message as MessageModel
from channels.db import database_sync_to_async

class MessageService(Service):
    '''
    Clase que representa el servicio de la entidad Group
    param:
        - Service: Clase que hereda de la interfaz Service
    '''

    def __init__(self):
        self.__repository = MessageRepository()

    @database_sync_to_async
    def add(self, message, user_id, username, group):
        message = MessageModel(
            message=message,
            user_id=user_id,
            username=username,
            group=group,
        )
        return self.__repository.create(message)
        
    def get_all(self):
        return self.__repository.find_all()

    def get_by_id(self, id):
        return self.__repository.find_by_id(id = id)
    
    def get_by_group_id_order_by_date(self, groupModel):
        return self.__repository.find_by_group_id_order_by_date(groupModel)