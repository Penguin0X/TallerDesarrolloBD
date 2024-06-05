from django import forms
from .models import User

TRABAJOS = [
    ('type1', 'Bodega'),
    ('type2', 'Empaque'),
    ('type3', 'Administración'),
    # añadir más después
]

class RegistroNuevoUser(forms.ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['nombre', 'apellido', 'email', 'username', 'contrasena', 'TipoTrabajo', 'LugarTrabajo']
        widgets = {
            'TipoTrabajo': forms.Select(choices=TRABAJOS)
        }
