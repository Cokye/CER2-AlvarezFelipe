from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import get_object_or_404


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre

class Comunicado(models.Model):
    NIVEL_CHOICES = [
    ("GEN", "General"),
    ("PRE", "Ciclo Preescolar"),
    ("BAS", "Ciclo Basico"),
    ("MED", "Ciclo Medio"),
]
    #identificador
    titulo= models.CharField(max_length=30)
    detalle= models.CharField(max_length=128)
    nivel= models.CharField(max_length=3, choices=NIVEL_CHOICES)
    fkcategoria= models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_envio= models.DateField()
    fecha_ultima= models.DateField()
    usuario= AbstractUser.username

    def __str__(self):
        return self.titulo