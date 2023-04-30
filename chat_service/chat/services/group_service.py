from ..repositories.group_repository import GroupRepository
from .services import Service

class GroupService(Service):
    '''
    Clase que representa el servicio de la entidad Group
    param:
        - Service: Clase que hereda de la interfaz Service
    '''

    def __init__(self):
        self.__repository = GroupRepository()

    def add(self, model):
        return self.__repository.create(model)
        
    def get_all(self):
        return self.__repository.find_all()

    def get_by_id(self, id):
        return self.__repository.find_by_id(id = id)