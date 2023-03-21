from django.db import models

# Message model with id, message, date, user_id, group_to.
class Message(models.model):
    id = models.AutoField(primary_key=True, unique=True)
    message = models.CharField(max_length=100, null=False)
    date = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField(max_length=100, null=False)
    username = models.CharField(max_length=20, null=False)
    group_to = models.CharField(max_length=20, null=False)