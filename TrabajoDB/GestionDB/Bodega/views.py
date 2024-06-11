from django.shortcuts import render, get_object_or_404, redirect
from .models import Juego,Consola,Estado  
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
        form = EditarJuegos(request.POST,request.FILES, instance=juego)
        if form.is_valid():
            form.save()
            messages.success(request, 'Juego actualizado exitosamente.')
            return redirect('lista_juegos')
    else:
        form = EditarJuegos(instance=juego)
    return render(request, 'bodega/editar_juego.html', {'form': form})

def eliminar_juego(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    if request.method == 'POST':
        juego.delete()
        messages.success(request, 'Juego eliminado exitosamente.')
        return redirect('lista_juegos')
    return render(request, 'bodega/eliminar_juego.html', {'juego': juego})

def buscar_juego(request):
    if request.method == 'GET':
        juegos = []
        filtro = request.GET.get("filtro")
        buscar = request.GET.get("searchInput")
        
        if filtro == 'Consola':
            juegos = Juego.objects.filter(consola={'nombreConsola':buscar})
        
        elif filtro == 'nombreJuego':
            juegos = Juego.objects.filter(nombreJuego__icontains=buscar)
            
        else:
            messages.error(request,"Error con la busqueda")
            juegos = Juego.objects.none()

    return render(request, 'bodega/lista_juegos.html', {'juegos': juegos})

def aumentarJuego(request,pk):
    juego = get_object_or_404(Juego, pk=pk)
    if request.method == 'GET':
        juego.unidades['cantidad'] += 1
        if juego.unidades['cantidad'] > 0:
            estados = Estado.objects.get(pk=0)
            juego.estado = {
                'id': estados.id,
                'nombreEstado':estados.nombreEstado
                }
            
        juego.save()
        

    juegos = Juego.objects.all()
    return render(request, 'bodega/lista_juegos.html', {'juegos': juegos})

def disminuirJuego(request,pk):
    juego = get_object_or_404(Juego, pk=pk)
    if request.method == 'GET':
        if juego.unidades['cantidad'] <= 0:
            messages.warning(request, 'El Juego ya esta en 0')
        else:
            juego.unidades['cantidad'] -= 1
            print(juego.unidades)
            if juego.unidades['cantidad'] == 0:
                estados = Estado.objects.get(pk=1)
                juego.estado = {
                    'id': estados.id,
                    'nombreEstado':estados.nombreEstado
                    }
            juego.save()
                


    juegos = Juego.objects.all()
    return render(request, 'bodega/lista_juegos.html', {'juegos': juegos})
        