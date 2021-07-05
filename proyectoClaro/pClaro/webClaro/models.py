from django.contrib.auth.backends import UserModel
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db.models.base import Model

# Create your models here.
class Comuna(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class ComunasSexta(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class ComunasMetropolitana(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=13)
    servicioContratado = models.CharField(max_length=20)
    tecnologiaServicio = models.CharField(max_length=4)
    planContratado = models.CharField(max_length=30)
    cantidadDecos = models.CharField(max_length=1)
    costoInstalacion = models.IntegerField()
    fechaInstalacion = models.DateField()
    vendedor = models.CharField(max_length=20)
    servicioTecnologia = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    Comuna = models.CharField(max_length=40)
    comentarios = models.CharField(max_length=300)

    def __str__(self):
        return self.rut

class ImagenPerfil(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='imgPerfil')

    def __str__(self):
        return self.imagen.url

class ServicioContratado(models.Model):
    nombre = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return self.nombre

class TecnologiaServicio(models.Model):
    nombre = models.CharField(primary_key=True, max_length=40)
    
    def __str__(self):
        return self.nombre

class PlanContratado(models.Model):
    nombre = models.CharField(primary_key=True, max_length=100)
    
    def __str__(self):
        return self.nombre

class CantidadDecodificadores(models.Model):
    nombre = models.CharField(primary_key=True, max_length=1)
    
    def __str__(self):
        return self.nombre

class EstadoInstalacion(models.Model):
    nombre = models.CharField(primary_key=True, max_length=20)
    
    def __str__(self):
        return self.nombre
