from django.shortcuts import render, get_object_or_404, redirect
from .models import Juego,Consola  
from .forms import FormJuegos,EditarJuegos
from django.contrib import messages

def lista_juegos(request):
    juegos = Juego.objects.all()
    return render(request, 'bodega/lista_juegos.html', {'juegos': juegos})

def agregar_juego(request):
    if request.method == 'POST':
        form = FormJuegos(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Juego añadido exitosamente.')
            return redirect('lista_juegos')
    
    else:
        form = FormJuegos()
    
    return render(request, 'bodega/agregar_juego.html', {'form': form})

def editar_juego(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    form = EditarJuegos(instance=juego)
    if request.method == 'POST':
        form = EditarJuegos(request.POST, instance=juego)
        if form.is_valid():
            form.save()
            messages.success(request, 'Juego actualizado exitosamente.')
            return redirect('lista_juegos')
    else:
        form = FormJuegos(instance=juego)
    return render(request, 'bodega/editar_juego.html', {'form': form})

def eliminar_juego(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    if request.method == 'POST':
        juego.delete()
        messages.success(request, 'Juego eliminado exitosamente.')
        return redirect('lista_juegos')
    return render(request, 'bodega/eliminar_juego.html', {'juego': juego})