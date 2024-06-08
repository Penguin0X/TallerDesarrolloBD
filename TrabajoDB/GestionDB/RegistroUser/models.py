from djongo import models
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect

# Create your models here.

class Rol(models.Model):
    
    id = models.IntegerField(primary_key=True,default=None)
    nombreRol = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreRol

class User(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)
    rol = models.EmbeddedField(model_container=Rol)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.username})"

