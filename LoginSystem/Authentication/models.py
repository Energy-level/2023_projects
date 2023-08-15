from django.db import models

# Create your models here.
class LoginData(models.Model):
    username=models.CharField(max_length=20)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password=models.IntegerField