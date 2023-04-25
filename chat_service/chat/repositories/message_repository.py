from .database import Database
from .repository import Create, Delete, Read, Update 
from ..models import Message as MessageModel
from ..models import Group as GroupModel

# TODO: Implementar delete en caso de agregar administrador para eliminar cursos.
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
    
    def create(self, message, user):
        group = GroupModel.objects.get(id=self.group_id)
        message = MessageModel(
            message=message,
            user_id=user.id,
            username=user.username,
            group=group,
        )
        message.save()

    def find_all(self):
        return MessageModel.objects.all()

    def find_by_id(self, id):
        return MessageModel.objects.get(id=id)