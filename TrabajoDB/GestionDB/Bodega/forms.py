from django import forms
from .models import Juego, Rol, Personal, Ubicacion, Stock, Estado, Consola, Distribucion

class FormJuegos(forms.ModelForm):
    
    class Meta:
        model = Juego
        fields = ('codigoDeBarra','nombreJuego','imagen')
        
    consola = forms.ModelChoiceField(queryset=Consola.objects.all(), label="Consola")
    distribucion = forms.ModelChoiceField(queryset=Distribucion.objects.all(), label="Distribuicion")
     
    imagen = forms.ImageField()
    
class FormRol(forms.ModelForm):
    class Meta:
        model = Rol
        fields = '__all__'

class FormPersonal(forms.ModelForm):
    class Meta:
        model = Personal
        fields = '__all__'

class FormUbicacion(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = '__all__'

class FormStock(forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'

class FormEstado(forms.ModelForm):
    class Meta:
        model = Estado
        fields = '__all__'

class FormConsola(forms.ModelForm):
    class Meta:
        model = Consola
        fields = '__all__'

class FormDistribucion(forms.ModelForm):
    class Meta:
        model = Distribucion
        fields = '__all__'