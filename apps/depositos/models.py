from django.db import models

# Create your models here.

class Deposito(models.Model):
    nombre = models.CharField(max_length=24, unique=True)
    observacion = models.TextField()
    encargado = models.CharField(max_length=24)
    
    
class Ubicacion(models.Model):
    nombre = models.CharField(max_length=24)
    deposito = models.OneToOneField('Deposito')
