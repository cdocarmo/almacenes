from django import forms

class AltaDeUsuario(forms.Form):
    
    nombre = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    telefono = forms.CharField(max_length=8)
    celular = forms.CharField(max_length=9)
    domicilio = forms.CharField(max_length=64) 
