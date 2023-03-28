# Test Unitario para la base de datos de la aplicación Django

import pytest
from chat.models import Message, Group

@pytest.mark.django_db
def test_group_creation():
    '''
    Test para crear un grupo en la base de datos
    '''
    Group.objects.create(name='test1')
    Group.objects.create(name='test2')


@pytest.mark.django_db
def test_get_group():
    '''
    Test para obtener un grupo de la base de datos
    '''
    Group.objects.create(name='test1')
    Group.objects.create(name='test2')
    group1 = Group.objects.get(name='test1')
    group2 = Group.objects.get(name='test2')
    assert group1.name == 'test1'
    assert group2.name == 'test2'
    assert group1.id > 0
    assert group2.id > 0


@pytest.mark.django_db
def test_message_creation():
    '''
    Test para crear un mensaje en la base de datos
    '''
    group_1 = Group.objects.create(name='test1')
    group_2 = Group.objects.create(name='test2')
    Message.objects.create(message='test1', user_id=1, username='test1', group=group_1)
    Message.objects.create(message='test2', user_id=2, username='test2', group=group_2)


@pytest.mark.django_db
def test_get_message():
    '''
    Test para obtener un mensaje de la base de datos
    '''
    group_1 = Group.objects.create(name='test1')
    group_2 = Group.objects.create(name='test2')
    Message.objects.create(message='test1', user_id=1, username='test1', group=group_1),
    Message.objects.create(message='test2', user_id=2, username='test2', group=group_2),
    message1 = Message.objects.get(message='test1')
    message2 = Message.objects.get(message='test2')
    assert message1.message == 'test1'
    assert message2.message == 'test2'
    assert message1.user_id == 1
    assert message2.user_id == 2
    assert message1.username == 'test1'
    assert message2.username == 'test2'

    assert message1.id > 0
    assert message2.id > 0