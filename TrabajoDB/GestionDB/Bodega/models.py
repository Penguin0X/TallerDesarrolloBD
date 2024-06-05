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
    nombreUbicacion = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.idUbicacion

class Stock(models.Model):
    ubicacion = models.CharField(max_length=100)
    cantidad = models.IntegerField(primary_key=True)

    def __str__(self):
        return f"Stock: {self.cantidad} unidades en {self.ubicacion}"

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
        return self.nombreConsola

class Distribucion(models.Model):
    LocalidadDistribucion = models.CharField(max_length=100)
    siglaDistribucion = models.CharField(max_length=5)

    def __str__(self):
        return self.LocalidadDistribucion

class Juego(models.Model):
    codigoDeBarra = models.IntegerField(unique=True)
    nombreJuego = models.CharField(max_length=250)
    consola = models.EmbeddedField(model_container=Consola)
    distribucion = models.CharField(max_length=5) # Region Juego
    estado = models.CharField(max_length=100) # Estados (Descontinuado - Sin Stock - ETC)
    unidades = models.EmbeddedField(model_container=Stock)
    imagen = models.ImageField()

    def __str__(self):
        return self.nombreJuego