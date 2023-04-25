from ..repositories.group_repository import GroupRepository
from ..services.services import Service

repository = GroupRepository()

class GroupService(Service):
    '''
    Clase que representa el servicio de la entidad Group
    param:
        - Service: Clase que hereda de la interfaz Service
    '''

    def add(self, model):
        return repository.create(model)
        
    def get_all(self):
        return repository.find_all()

    def get_by_id(self, id):
        return repository.find_by_id(id = id)