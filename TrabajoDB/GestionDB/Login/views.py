from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect,get_object_or_404
from RegistroUser.models import User
from .forms import LoginForm
from django.contrib.auth import authenticate,login

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('contrasena')
            user = User.objects.get(username=username)
            if user is not None:
                check = check_password(password,password)
                if check is not None:
                    if user.rol['id'] == 2:
                        return redirect('bodega/')
                    
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})