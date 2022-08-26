from datetime import date
from django.db import models
from datetime import datetime
# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=122)
    password=models.CharField(max_length=122,default="room")
class chatMessage(models.Model):
    message=models.CharField(max_length=122)
    datetime=models.DateTimeField(default=datetime.now,blank="True")
    username=models.CharField(max_length=122)
    room_id=models.CharField(max_length=122)
