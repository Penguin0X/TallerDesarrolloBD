from django import forms
from .models import Juego, Rol, Personal, Ubicacion, Stock, Estado, Consola, Distribucion


class FormConsola(forms.ModelForm):
    class Meta:
        model = Consola
        fields = '__all__'

class FormJuegos(forms.ModelForm):
        
    class Meta:
        model = Juego
        fields =('codigoDeBarra','nombreJuego','imagen')
    
    codigoDeBarra = forms.IntegerField()
    nombreJuego = forms.CharField()
    imagen = forms.ImageField()
    
    Plataforma = forms.ModelChoiceField(queryset=Consola.objects.all(), empty_label="Seleccionar Plataforma")
    Región = forms.ModelChoiceField(queryset=Distribucion.objects.all(), empty_label="Seleccionar Región")
    
    def save(self, commit=True):
        juego = super().save(commit=False)
        
        consolaSeleccionada = self.cleaned_data['Plataforma']
        regionSeleccionada = self.cleaned_data['Región']

        consolaEncontrada = Consola.objects.get(pk=consolaSeleccionada.id)
        regionEncontrada = Distribucion.objects.get(pk=regionSeleccionada.id)
        juego.consola = {
            'id':consolaEncontrada.id,
            'nombreConsola':consolaEncontrada.nombreConsola,
            'marcaConsola':consolaEncontrada.marcaConsola
        }
        juego.distribucion = {
            'id': regionEncontrada.id,
            'localidadDistribucion':regionEncontrada.localidadDistribucion,
            'siglaDistribucion':regionEncontrada.siglaDistribucion
        }
        
        if commit:
            juego.save()
        
class EditarJuegos(forms.ModelForm):
    
    class Meta:
        model = Juego
        fields =['codigoDeBarra','nombreJuego','imagen','estado',]
        

    
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

class FormDistribucion(forms.ModelForm):
    class Meta:
        model = Distribucion
        fields = '__all__'