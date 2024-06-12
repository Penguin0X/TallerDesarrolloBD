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
            password = form.cleaned_data.get('password')
            user = User.objects.get(username=username)
            if user:
                check = check_password(password,user.contrasena)
                print(password)
                print(check)
                if check == True:
                    if user.rol['id'] == 2:
                        return redirect('bodega/')
                if check == False:
                    messages.warning(request,"Contraseña Incorrecta")
            elif User.DoesNotExist:
                print("Logica correcta")
                    
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})