from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.rol.models import Roles
from django.db.models import SET_NULL

# Create your models here.
class User(AbstractUser):
    cedula = models.IntegerField(max_length=20,unique=True) 
    fk_rol = models.ForeignKey(Roles, on_delete=SET_NULL,null=True)
    edad = models.IntegerField(max_length=20)
    def __str__(self):
        return self.username