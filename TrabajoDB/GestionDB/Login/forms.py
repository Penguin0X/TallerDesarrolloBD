from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Nombre Usuario",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username'})
    )
    password  = forms.CharField(
        label="Contraseña",
        max_length=100,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'contrasena'})
    )
