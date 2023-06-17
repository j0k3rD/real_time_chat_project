from .repository import Create, Delete, Read, Update 
from ..models import Message as MessageModel
from channels.db import database_sync_to_async
import json

class MessageRepository(Create, Read):
    '''
    Clase que representa el repositorio de la entidad Message
    param:
        - Create: Clase que hereda de la interfaz Create
        - Read: Clase que hereda de la interfaz Read
        - Update: Clase que hereda de la interfaz Update
    '''
    def __init__(self):
        self.__type_model = MessageModel

    @property
    def type_model(self):
        return self.__type_model
    
    @database_sync_to_async
    def create(self, model):
        model = MessageModel(
            message = model.message,
            user_id = model.user_id,
            username = model.username,
            group = model.group
        )
        print('guardado modelo', model)
        return model.save()

    def find_all(self):
        return MessageModel.objects.all()

    def find_by_id(self, id):
        return MessageModel.objects.get(id=id)
    
    def find_by_group_id_order_by_date(self, groupModel):
        return MessageModel.objects.filter(group=groupModel).order_by('date')