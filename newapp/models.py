from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Visitor(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=5)
    age=models.IntegerField()
    number=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Message(models.Model):
    leavemessage=models.TextField(max_length=10000)
    pubtime=models.DateTimeField('-date published')
    username=models.CharField(max_length=20)
    title=models.CharField(max_length=30)
    image=models.ImageField(max_length=255,upload_to='newapp/static/newapp/userupload/')
    def __str__(self):
        return self.title
