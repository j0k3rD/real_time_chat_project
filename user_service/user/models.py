from django.db import models

# User model with id, username, password, email.
class User(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=20, null=False, unique=True)
    password = models.CharField(max_length=500, null=False)
    email = models.EmailField(max_length=50, null=False, unique=True)