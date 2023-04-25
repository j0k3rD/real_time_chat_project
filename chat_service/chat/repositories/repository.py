from abc import ABC, abstractmethod
from .. import db

# Clase abstracta que define los métodos que deben implementar las clases que hereden de ella.

class Create(ABC):
    '''
    Clase con los métodos abstractos para crear un modelo
    param:
        - ABC: Clase de la cual hereda que es abstracta.
    '''
    @abstractmethod  
    def create(self, model: db.Model):
        '''
        Método abstracto para crear un modelo
        
        param:
            - model: Modelo a crear
        '''
        pass

class Read(ABC):
    '''
    Clase con los métodos abstractos para leer un modelo
    param:
        - ABC: Clase de la cual hereda que es abstracta.
    '''
    @abstractmethod
    def find_all(self):
        '''
        Método abstracto para encontrar todos los modelos
        '''
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> db.Model:
        '''
        Método abstracto para encontrar un modelo por su id
        '''
        pass

class Update(ABC):
    '''
    Clase con los métodos abstractos para actualizar un modelo
    param:
        - ABC: Clase de la cual hereda que es abstracta.
    '''
    @abstractmethod
    def update(self, model: db.Model) -> db.Model:
        '''
        Método abstracto para actualizar un modelo
        '''
        pass

class Delete(ABC):
    '''
    Clase con los métodos abstractos para eliminar un modelo
    param:
        - ABC: Clase de la cual hereda que es abstracta.
    '''
    @abstractmethod
    def delete(self, model: db.Model):
        '''
        Método abstracto para eliminar un modelo
        '''
        pass 

    @abstractmethod
    def delete_by_id(self, id: int):
        '''
        Método abstracto para eliminar un modelo por su id
        '''
        pass