from django.db import models

# Create your models here.

class Deposito(models.Model):
    nombre = models.CharField(max_length=24, unique=True)
    observacion = models.TextField()
    encargado = models.CharField(max_length=24)
    
    def __unicode__(self):
        return self.nombre
    
    
class Ubicacion(models.Model):
    nombre = models.CharField('Ubicacion', max_length=24)
    deposito = models.OneToOneField('Deposito')
    
    def __unicode__(self):
        return self.nombre
