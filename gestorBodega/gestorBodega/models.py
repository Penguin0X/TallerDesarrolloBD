from django.db import models

class Rol(models.Model):
    idRol= models.AutoField ()
    nombreRol = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreRol

class Personal(models.Model):
    idPersona = models.AutoField() 
    nombrePersonal = models.CharField(max_length=255)
    rolId = models.CharField(max_length=255)
    telefono = models.IntegerField(unique=True, validators=[RegexValidator(r'^[0-9]{8}$')])
    usuarios = models.CharField(max_length=255)
    contraseña = models.CharField(max_length=128, validators=[MinLengthValidator(8), RegexValidator(r'^[a-zA-Z0-9]+$')])

    def __str__(self):
        return self.idPersona

class Ubicacion(models.Model):
    idUbicacion=models.AutoField
    nombreUbicacion=models.CharField
    descripcion=models.CharField

    def __str__(self):
        return self.idUbicacion

class Stock(models.Model):
    Ubicacion= models.CharField
    cantidad= models.IntegerField

    def __str__(self):
        return f"Stock: {self.cantidad} unidades en {self.ubicacion.nombreUbicacion}"

    def restar_cantidad(self, unidades_a_restar):
        self.cantidad -= unidades_a_restar

    def aumentar_cantidad(self, unidades_a_agregar):
        self.cantidad += unidades_a_agregar

class Estado(models.Model):
    idEstado=models.AutoField
    nombreEstado=models.CharField(max_length=100)

    def __str__(self):
        return f"Estado: {self.nombreEstado}"

class Consola(models.Model):
    idConsola=models.AutoField
    NombreConsola = models.CharField(max_length=100)
    MarcaConsola = models.CharField(max_length=100)

class Distribucion():
    idDistribucion=models.AutoField
    LocalidadDistribucion = models.CharField(max_length=100)
    siglaDistribucion = models.CharField(max_length=5)


class Juego(models.Model):    
    codigoDeBarra = models.IntegerField(unique=True)
    nombreJuego = models.CharField(max_length=250)
    consola = models.CharField (max_length=100)
    distribucion = models.CharField(max_length=5)
    estado = models.CharField(max_length=100)
    stock = models.ManyToManyField
    imagen=models.ImageField 
    
    def __str__(self):
        return self.nombreJuego
