from typing import Any
from django.db import models
from djongo import models
from django.core.validators import RegexValidator, MinLengthValidator

class Rol(models.Model):
    nombreRol = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreRol

class Personal(models.Model):
    nombrePersonal = models.CharField(max_length=255)
    rolId = models.CharField(max_length=255)
    telefono = models.IntegerField(unique=True, validators=[RegexValidator(r'^[0-9]{8}$')])
    usuarios = models.CharField(max_length=255)
    contraseña = models.CharField(max_length=128, validators=[MinLengthValidator(8), RegexValidator(r'^[a-zA-Z0-9]+$')])

    def __str__(self):
        return self.idPersona

class Ubicacion(models.Model):
    
    _id = models.IntegerField(primary_key=True, default=None)
    nombreUbicacion = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.nombreUbicacion)

class Stock(models.Model):
    
    ubicacion = models.CharField(max_length=100)
    cantidad = models.IntegerField(primary_key=True)

    def __str__(self):
        return "{}".format(self.cantidad)

    def restar_cantidad(self, unidades_a_restar):
        self.cantidad -= unidades_a_restar

    def aumentar_cantidad(self, unidades_a_agregar):
        self.cantidad += unidades_a_agregar

class Estado(models.Model):
    nombreEstado = models.CharField(max_length=100)

    def __str__(self):
        return f"Estado: {self.nombreEstado}"

class Consola(models.Model):

    id = models.IntegerField(primary_key=True, default=None)
    nombreConsola = models.CharField(max_length=100)
    marcaConsola = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.nombreConsola)

class Distribucion(models.Model):
    
    id = models.IntegerField(primary_key=True, default=None)
    localidadDistribucion = models.CharField(max_length=80)
    siglaDistribucion = models.CharField(max_length=5)

    def __str__(self):
        return "{}".format(self.siglaDistribucion+" : "+self.localidadDistribucion)

class Juego(models.Model):
    codigoDeBarra = models.IntegerField(unique=True)
    nombreJuego = models.CharField(max_length=250)
    consola = models.EmbeddedField(model_container=Consola)
    distribucion = models.EmbeddedField(model_container=Distribucion) # Region Juego
    estado = models.CharField(max_length=100) # Estados (Descontinuado - Sin Stock - ETC)
    unidades = models.EmbeddedField(model_container=Stock)
    ubicacion = models.EmbeddedField(model_container=Ubicacion)
    imagen = models.ImageField(upload_to='juegos/')

    def __str__(self):
        return self.nombreJuego