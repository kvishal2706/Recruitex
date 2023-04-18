from django.db import models
from datetime import datetime
from accounts.models import CustomUser

class Room(models.Model):
    users=models.ManyToManyField('accounts.CustomUser')
    
    
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)