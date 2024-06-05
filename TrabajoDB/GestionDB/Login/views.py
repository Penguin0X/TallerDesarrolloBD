from django.contrib import messages
from django.shortcuts import render, redirect
from RegistroUser.models import User
from .forms import LoginForm
import pymongo

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            find = User.objects.get(username=username)
            passcheck = find.contrasena
            if password==passcheck:
                return redirect('bodega/')

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})