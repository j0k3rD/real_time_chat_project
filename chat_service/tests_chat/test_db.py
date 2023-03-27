# Test Unitario para la base de datos de la aplicación Django

import pytest
from chat.models import Message

@pytest.mark.django_db
def test_chat_creation():
    '''
    Test para crear un mensaje en la base de datos
    '''
    Message.objects.create(message='test1', user_id=1, username='test1', group_to='test1'),
    Message.objects.create(message='test2', user_id=2, username='test2', group_to='test2'),

@pytest.mark.django_db
def test_get_message():
    '''
    Test para obtener un mensaje de la base de datos
    '''
    Message.objects.create(message='test1', user_id=1, username='test1', group_to='test1'),
    Message.objects.create(message='test2', user_id=2, username='test2', group_to='test2'),
    message1 = Message.objects.get(message='test1')
    message2 = Message.objects.get(message='test2')
    assert message1.message == 'test1'
    assert message2.message == 'test2'
    assert message1.user_id == 1
    assert message2.user_id == 2
    assert message1.username == 'test1'
    assert message2.username == 'test2'
    assert message1.group_to == 'test1'
    assert message2.group_to == 'test2'

    assert message1.id > 0