# Creamos el repositorio de la entidad Group, para Django y MySQL
from .database import Database
from .repository import Create, Delete, Read, Update 
from ..models import Group as GroupModel

# TODO: Implementar delete en caso de agregar administrador para eliminar cursos.
class GroupRepository(Create, Read, Update):
    '''
    Clase que representa el repositorio de la entidad Group
    param:
        - Create: Clase que hereda de la interfaz Create
        - Read: Clase que hereda de la interfaz Read
        - Update: Clase que hereda de la interfaz Update
    '''
    def __init__(self):
        self.__type_model = GroupModel

    @property
    def type_model(self):
        return self.__type_model
    
    def create(self):

    def update(self):

    def find_all(self):

    def find_by_id(self):