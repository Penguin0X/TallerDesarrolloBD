from django.shortcuts import render, redirect
from .forms import RegistroNuevoUser
from django.contrib import messages

def registrar_user(request):
    if request.method == 'POST':
        form = RegistroNuevoUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('registro_user')  # Devuleve al registro
        else:
            # Error
            messages.error(request, 'Hubo un error al registrar el usuario. Por favor, revise los datos ingresados.')
    else:
        form = RegistroNuevoUser()
    return render(request, 'registro_user.html', {'form': form})