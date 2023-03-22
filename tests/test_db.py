# Test Unitario para la base de datos de la aplicación Django

from django.test import TestCase
from ..chat_service.chat.models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="pedrito123", password="sisisi", email="pedrito@gmail.com")
        User.objects.create(username="ramon123", password="sisi2", email="ramon@gmail.com")