from django.contrib import messages
from django.shortcuts import render, redirect
from RegistroUser.models import User
from .forms import LoginForm
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('contrasena')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Check if the user has a job type
                if hasattr(user, 'TipoTrabajo'):
                    # Redirect based on the user's job type
                    if user.TipoTrabajo == 'type1': 
                        return redirect('lista_juegos')
                    # lif user.tipo_trabajo == 'otro':
                        # return redirect('otra_pagina')
                else:
                    messages.error(request, 'Error de sistema.')
                    return render(request, 'login.html', {'form': form})
            else:
                messages.error(request, 'Usuario no encontrado. Verifique su nombre de usuario y contraseña.')
                return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})