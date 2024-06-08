from django.contrib import admin
from .models import Personal, Ubicacion, Stock, Estado, Consola, Distribucion, Juego

# Register your models here.

class PersonalAdmin(admin.ModelAdmin):
    list_display = ['nombrePersonal', 'rolId', 'telefono', 'usuarios']

class UbicacionAdmin(admin.ModelAdmin):
    list_display = ['nombreUbicacion', 'descripcion']

class StockAdmin(admin.ModelAdmin):
    list_display = ['ubicacion', 'cantidad']

class EstadoAdmin(admin.ModelAdmin):
    list_display = ['nombreEstado']

class ConsolaAdmin(admin.ModelAdmin):
    list_display = ['nombreConsola', 'marcaConsola']

class DistribucionAdmin(admin.ModelAdmin):
    list_display = ['localidadDistribucion', 'siglaDistribucion']

class JuegoAdmin(admin.ModelAdmin):
    list_display = ['codigoDeBarra', 'nombreJuego', 'consola', 'distribucion', 'estado', 'unidades']

admin.site.register(Personal, PersonalAdmin)
admin.site.register(Ubicacion, UbicacionAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Consola, ConsolaAdmin)
admin.site.register(Distribucion, DistribucionAdmin)
admin.site.register(Juego, JuegoAdmin)
