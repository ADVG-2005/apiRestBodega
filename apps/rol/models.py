from django.db import models

# Create your models here.
class Roles(models.Model):
    ROL_CHOICE = {
        ('Tecnico','Tecnico'),
        ('Catador','Catador'),
        ('Barista','Barista')
    }

    rol = models.CharField(max_length=20,choices=ROL_CHOICE)
    def __str__(self):
        return self.rol