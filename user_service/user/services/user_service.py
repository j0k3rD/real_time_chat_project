from ..repositories.user_repository import UserRepository
from .services import Service
from django.contrib.auth.hashers import make_password, check_password
from ..models import User as UserModel

class UserService(Service):
    '''
    Clase que representa el servicio de la entidad Message
    param:
        - Service: Clase que hereda de la interfaz Service
    '''

    def __init__(self):
        self.__repository = UserRepository()

    def add(self, username, email, password):
        return self.__repository.create(username, email, password)
        
    def get_all(self):
        return self.__repository.find_all()

    def get_by_id(self, id):
        return self.__repository.find_by_id(id = id)
    
    def get_by_email(self, email):
        return self.__repository.find_by_email(email = email)
    
    def check_password(self, password, user_password):
        return check_password(password, user_password)
    
    def check_user_email(self, email):
        return self.__repository.check_user_email(email = email)
    
    def check_user_username(self, username):
        return self.__repository.check_user_username(username = username)