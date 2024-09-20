from django.db import models

# Create your models here.
class Materiales(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    fechaIngreso =models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
