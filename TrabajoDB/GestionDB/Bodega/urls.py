from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_juegos, name='lista_juegos'),
    path('agregar/', views.agregar_juego, name='agregar_juego'),
    path('editar/<int:pk>/', views.editar_juego, name='editar_juego'),
    path('buscar/', views.buscar_juego, name='buscar'),
    path('eliminar/<int:pk>/', views.eliminar_juego, name='eliminar_juego'),
    path('aumentar/<int:pk>/', views.aumentarJuego, name='aumentar'),
    path('disminuir/<int:pk>/', views.disminuirJuego, name='disminuir'),
]