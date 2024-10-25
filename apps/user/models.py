from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    cedula = models.IntegerField(unique=True,null=True) 
    edad = models.IntegerField(null=True)
    def __str__(self):
        return self.username