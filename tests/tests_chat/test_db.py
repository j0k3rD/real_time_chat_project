# Test Unitario para la base de datos de la aplicación Django

from django.test import TestCase
from ...chat_service.chat.models import Messages


class TestMessages(TestCase):
    def setUp(self):
        Message.objects.create(message='test1', user_id=1, username='test1', group_to='test1'),
        Message.objects.create(message='test2', user_id=2, username='test2', group_to='test2'),

    def test_message(self):
        message1 = Message.objects.get(message='test1')
        message2 = Message.objects.get(message='test2')
        self.assertEqual(message1.message, 'test1')
        self.assertEqual(message2.message, 'test2')
        self.assertEqual(message1.user_id, 1)
        self.assertEqual(message2.user_id, 2)
        self.assertEqual(message1.username, 'test1')
        self.assertEqual(message2.username, 'test2')
        self.assertEqual(message1.group_to, 'test1')
        self.assertEqual(message2.group_to, 'test2')