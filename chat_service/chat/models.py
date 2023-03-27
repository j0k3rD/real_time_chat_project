from django.db import models

# Group model with id, name.
class Group(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=25, null=False)

# Message model with id, message, date, user_id, group_to.
class Message(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    message = models.CharField(max_length=100, null=False)
    date = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField(null=False)
    username = models.CharField(max_length=20, null=False)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, null=False)