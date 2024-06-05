from django.db import models

# Create your models here.

class User(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)
    TipoTrabajo = models.CharField(max_length=100)
    LugarTrabajo = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.username})"