from django import forms
from .models import User
from .models import Rol
from django.contrib.auth.hashers import make_password

class RegistroNuevoUser(forms.ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput())
    posicion = forms.ModelChoiceField(queryset=Rol.objects.exclude(nombreRol='dueño'))

    class Meta:
        model = User
        fields = ['nombre', 'apellido', 'email', 'username', 'contrasena']
        
    def save(self, commit=True):
        usuario = super().save(commit=False)
        
        rolSeleccionado = self.cleaned_data['posicion']
        
        usuario.rol = {
            'id':rolSeleccionado.id,
            'nombreRol':rolSeleccionado.nombreRol
        }
        usuario.contrasena = make_password(self.cleaned_data['contrasena'])
        if commit:
            usuario.save()
            
