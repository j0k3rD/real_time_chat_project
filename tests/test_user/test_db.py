# Test Unitario para la base de datos de la aplicación Django

from django.test import TestCase
from ...user_service.user.model import User


class TestUsers(TestCase):
    def setUp(self):
        User.objects.create(username='test1', password='test1', email='test1@gmail.com'),
        User.objects.create(username='test2', password='test2', email='test2@gmail.com'),

    def test_user(self):
        user1 = User.objects.get(username='test1')
        user2 = User.objects.get(username='test2')
        self.assertEqual(user1.username, 'test1')
        self.assertEqual(user2.username, 'test2')
        self.assertEqual(user1.password, 'test1')
        self.assertEqual(user2.password, 'test2')
        self.assertEqual(user1.email, 'test1')
        self.assertEqual(user2.email, 'test2')


