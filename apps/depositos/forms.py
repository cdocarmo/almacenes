from django import forms
# from django.forms.models import inlineformset_factory
from django.db import models

from .models import Deposito, Ubicacion


class AltaDeDeposito(forms.ModelForm):
    class Meta:
        model = Deposito
        widgets = {
                   'nombre': forms.TextInput(attrs={'class': 'form-control'}),
                   'observacion': forms.Textarea(attrs={'class': 'form-control'}),
                   'encargado': forms.TextInput(attrs={'class': 'form-control'}),
                   }
        

class AltaDeUbicacion(forms.ModelForm):
        
    class Meta:
        model = Ubicacion
        widgets = {
                   'Ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
                   'deposito': forms.HiddenInput(),
                   }
        
        
# def formfield_callback(field):
#     if isinstance(field, models.CharField) and field.name == 'nombre':
#         return forms.fields.CharField(label='Ubicacion', widget=forms.TextInput(attrs={'class' : 'form-control'}))
#     if isinstance(field, models.BooleanField) and field.name == 'eliminar':
#         return forms.fields.CharField(widget=forms.TextInput(attrs={'class' : 'hide'}))
#     return field.formfield()
#         
# UbicacionFormSet = inlineformset_factory(Deposito, Ubicacion, formfield_callback = formfield_callback)
