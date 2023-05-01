from .repository import Create, Delete, Read, Update 
from django.contrib.auth import get_user_model
from ..models import User as UserModel

class UserRepository(Create, Read):
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
        user = get_user_model().objects.create_user(username=username, email=email, password=password)
        return user

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

    def check_user_email(self, email):
        return UserModel.objects.filter(email=email).exists()

    def check_user_username(self, username):
        return UserModel.objects.filter(username=username).exists()

    # def delete(self, id):
        # UserModel.objects.get(id=id).delete()