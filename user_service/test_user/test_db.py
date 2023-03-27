# Test Unitario para la base de datos de la aplicación Django

import pytest
from user.models import User

@pytest.mark.django_db
def test_user_creation():
    '''
    Test para la creación de usuarios en la base de datos
    '''
    User.objects.create(username='test1', password='test1', email='test1@gmail.com')
    User.objects.create(username='test2', password='test2', email='test2@gmail.com')

@pytest.mark.django_db
def test_get_user():
    '''
    Test para la obtención de usuarios en la base de datos
    '''
    User.objects.create(username='test1', password='test1', email='test1@gmail.com')
    user = User.objects.get(username='test1')
    assert user.username == 'test1'


