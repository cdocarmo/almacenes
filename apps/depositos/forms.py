from django import forms
from django.forms.models import inlineformset_factory

from .models import Deposito, Ubicacion


class AltaDeDeposito(forms.ModelForm):
    class Meta:
        model = Deposito
        
UbicacionFormSet = inlineformset_factory(Deposito, Ubicacion)
