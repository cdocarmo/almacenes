from django.db import models
from apps.depositos.models import Ubicacion # sera necesario

# Create your models here.

class ProductoDescripcion(models.Model):
    '''
    Este modelo es una descripcion del producto, es informacion que comparten
    todas las unidades del mismo producto.
    '''
    
    ORIGEN_CHOICES = (
                      ('NAC', 'Nacional'),
                      ('IMP', 'Importado'),
                      )
    
    nombre = models.CharField(max_length=24)
    marca = models.CharField(max_length=24)
    origen = models.CharField(max_length=3, choices=ORIGEN_CHOICES)
    
    # no se me ocurren otros campos... GF
    
class ProductoStock(models.Model):
    '''
    Este modelo lleva el conteo del stock.
    '''
    producto = models.ForeignKey('ProductoDescripcion')
    stock = models.IntegerField(default=0)
    
    
class ProductoUnidad(models.Model):
    '''
    Este modelo representa cada unidad y como tal su propio codigo de barras (si corresponde), 
    su vencimiento y ubicacion.
    '''
    codigo_barras = models.CharField(max_length=13)
    vencimiento = models.DateField()
    ubicacion = models.ForeignKey('depositos.Ubicacion')
    