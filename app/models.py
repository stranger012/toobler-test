from django.db import models

# Create your models here.


class User(models.Model):
    name=models.CharField(max_length=25)
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=25)

class Message(models.Model):
    content=models.CharField(max_length=500)
    username=models.CharField(max_length=25)
    created_date=models.DateField(auto_now_add=True)

class Activity(models.Model):
    content=models.CharField(max_length=100)
    created_date=models.DateField(auto_now_add=True)
    