from .database import Database
from .repository import Create, Delete, Read, Update 
from ..models import Message as UserModel
from django.contrib.auth.hashers import make_password, check_password


class UserRepository(Create, Read, Update):
    '''
    Clase que representa el repositorio de la entidad User
    param:
        - Create: Clase que hereda de la interfaz Create
        - Read: Clase que hereda de la interfaz Read
        - Update: Clase que hereda de la interfaz Update
    '''
    def __init__(self):
        self.__type_model = UserModel

    @property
    def type_model(self):
        return self.__type_model
    
    def create(self, username, email, password):
        user = UserModel(
            username=username,
            email=email,
            password=password,
        )
        user.password = make_password(password)
        user.save()

    # def update(self, id, username, email, password):
    #     user = UserModel.objects.get(id=id)
    #     user.username = username
    #     user.email = email
    #     user.password = make_password(password)
    #     user.save()

    def find_all(self):
        return UserModel.objects.all()

    def find_by_id(self, id):
        return UserModel.objects.get(id=id)
    
    def find_by_email(self, email):
        return UserModel.objects.get(email=email)

    # def delete(self, id):
        # UserModel.objects.get(id=id).delete()