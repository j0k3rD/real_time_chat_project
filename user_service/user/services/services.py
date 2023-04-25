from abc import ABC, abstractmethod

class Service(ABC):
    '''
    Clase abstracta que define los métodos que deben implementar las clases que hereden de ella.
    param:
        - ABC: Clase de la cual hereda que es abstracta.
    '''
    @abstractmethod  
    def add(self, model):
        '''
        Método abstracto para agregar un modelo
        param:
            - model: Modelo a agregar
        '''
        pass

    @abstractmethod    
    def get_all(self):
        '''
        Método abstracto para obtener todos los modelos
        '''
        pass

    @abstractmethod
    def get_by_id(self, id):
        '''
        Método abstracto para obtener un modelo por su id
        '''
        pass