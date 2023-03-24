#Test unitarios para la aplicación Django

from django.test import TestCase


class TestApp(TestCase):
    def test_app(self):
        self.assertEqual("real_time_chat_project", "real_time_chat_project")