from django.db import models

# Create your models here.

from django.db import models 

class Usuario(models.Model):
     id_user = models.IntegerField()
     name_user = models.CharField(max_length=50)
     password = models.CharField(max_length=8)
     nombre = models.CharField(max_length=50)
     apellido = models.CharField(max_length=50)
     correo = models.CharField(max_length=100)
     
     def __str__(self): 
         return self.nombre
