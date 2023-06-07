from django.db import models
from datetime import datetime as dt
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
class Room(models.Model):
    name = models.CharField(max_length=100)
    creater = models.CharField(max_length=100)
    date = models.DateTimeField(default=dt.now(),blank=True)

class Message(models.Model):
    msg = models.CharField(max_length=10000)
    room = models.CharField(max_length=100)
    sender = models.CharField(max_length=100)
    date = models.DateTimeField(default=dt.now(),blank=True)

class Map(models.Model):
    roomid = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

class Active(models.Model):
    roomid = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    online = models.BooleanField(default=True)
    active_display = models.BooleanField(default=False)
    offline_display = models.BooleanField(default=False)


class Ai_msg(models.Model):
    sno = models.AutoField(primary_key=True)
    user_msg = models.CharField(max_length=1000)

