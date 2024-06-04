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
    nombreUbicacion=models.CharField()
    descripcion=models.CharField()

    def __str__(self):
        return self.idUbicacion

class Stock(models.Model):
    Ubicacion= models.CharField(max_length=100)
    cantidad= models.IntegerField()

    def __str__(self):
        return f"Stock: {self.cantidad} unidades en {self.ubicacion.nombreUbicacion}"

    def restar_cantidad(self, unidades_a_restar):
        self.cantidad -= unidades_a_restar

    def aumentar_cantidad(self, unidades_a_agregar):
        self.cantidad += unidades_a_agregar

class Estado(models.Model):
    nombreEstado=models.CharField(max_length=100)

    def __str__(self):
        return f"Estado: {self.nombreEstado}"

class Consola(models.Model):
    id = models.IntegerField(primary_key=True, default=None)
    NombreConsola = models.CharField(max_length=100)
    MarcaConsola = models.CharField(max_length=100)

class Distribucion():
    
    LocalidadDistribucion = models.CharField(max_length=100)
    siglaDistribucion = models.CharField(max_length=5)

def __str__(self):
        return self.nombreConsola

class Juego(models.Model):
    
    codigoDeBarra = models.IntegerField(unique=True)
    nombreJuego = models.CharField(max_length=250)
    consola = models.EmbeddedField(model_container=Consola)
    distribucion = models.CharField(max_length=5) #Region Juego
    estado = models.CharField(max_length=100) #Estados (Descontinuado - Sin Stock - ETC)
    unidades = models.EmbeddedField(model_container=Stock)
    #cantidad
 #ubicacion (Estante en bodega).
    imagen=models.ImageField()
    
    def __str__(self):
        return self.nombreJuego

