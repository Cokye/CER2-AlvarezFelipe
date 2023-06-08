from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib import admin


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
    fecha_emision= models.DateField()
    fecha_modificacion= models.DateField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)

  
    def __str__(self):
        return self.titulo