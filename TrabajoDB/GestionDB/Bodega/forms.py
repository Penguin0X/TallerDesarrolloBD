from django import forms
from .models import Juego, Personal, Ubicacion, Stock, Estado, Consola, Distribucion


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
        fields =['codigoDeBarra','nombreJuego','imagen',]
    
    
    codigoDeBarra = forms.IntegerField()
    nombreJuego = forms.CharField()
    imagen = forms.ImageField()
    
    estado = forms.ModelChoiceField(queryset=Estado.objects.all(),empty_label="Seleccionar Estado")
    Plataforma = forms.ModelChoiceField(queryset=Consola.objects.all(), empty_label="Seleccionar Plataforma")
    Región = forms.ModelChoiceField(queryset=Distribucion.objects.all(), empty_label="Seleccionar Región")
    ubicacion = forms.ModelChoiceField(queryset=Ubicacion.objects.all(), empty_label="Seleccionar Ubicación")
    unidades = forms.IntegerField()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            
            estado_nombre = self.instance.estado
            if estado_nombre:
                try:
                    estado_nombre = self.instance.estado.get('nombreEstado')
                    self.fields['estado'].initial = Estado.objects.get(nombreEstado=estado_nombre)
                except:
                    pass
            plataforma_id = self.instance.consola.get('nombreConsola')
            
            self.fields['Plataforma'].initial = Consola.objects.get(nombreConsola=plataforma_id)
    
    def save(self, commit=True):
        juego = super().save(commit=False)
        
        estadoSeleccionado = self.cleaned_data['estado']
        consolaSeleccionada = self.cleaned_data['Plataforma']
        regionSeleccionada = self.cleaned_data['Región']
        ubicacionSeleccionada = self.cleaned_data['ubicacion']
        stock = self.cleaned_data['unidades']
        stockid = juego.id
        
        estadoEncontrado = Estado.objects.get(pk=estadoSeleccionado.id)
        consolaEncontrada = Consola.objects.get(pk=consolaSeleccionada.id)
        regionEncontrada = Distribucion.objects.get(pk=regionSeleccionada.id)
        ubicacionEncontrada = Ubicacion.objects.get(pk=ubicacionSeleccionada.id)
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
        juego.estado = {
            'id': estadoEncontrado.id,
            'nombreEstado':estadoEncontrado.nombreEstado
        }
        juego.ubicacion = {
            'id': ubicacionEncontrada.id,
            'nombreUbicacion':ubicacionEncontrada.nombreUbicacion,
            'descripcion':ubicacionEncontrada.descripcion
        }
        juego.unidades = {
            'id':stockid,
            'ubicacion':ubicacionEncontrada.nombreUbicacion,
            'cantidad':stock
        }
        if commit:
            juego.save()
        
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