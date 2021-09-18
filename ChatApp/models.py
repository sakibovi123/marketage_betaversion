from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from mainApp.models import *
# Create your models here.


class ChatRoom(models.Model):
    room_name = models.CharField(max_length=210, null=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    sellers = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="sellers")
    recent_chat = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.id)
    


class Message(models.Model):
    sent_date = models.DateTimeField(default=datetime.now)
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    msg = models.TextField(null=True)
    
    
    def __str__(self):
        return str(self.id)
    



# class Test(models.Model):
#     message = Charfield()

