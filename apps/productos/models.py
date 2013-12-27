from django.db import models
from apps.depositos.models import Ubicacion
from apps.proveedores.models import Proveedor

# Create your models here.

class Producto(models.Model):
    '''
    Este modelo es una descripcion del producto, es informacion que comparten
    todas las unidades del mismo producto.
    '''
    
    ORIGEN_CHOICES = (
                      ('NAC', 'Nacional'),
                      ('IMP', 'Importado'),
                      )
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=24)
    familia = models.CharField(max_length=24)
    subfamilia = models.CharField(max_length=24)
    marca = models.CharField(max_length=24)
    costo = models.DecimalField(max_digits=10, decimal_places=3)
    origen = models.CharField(max_length=3, choices=ORIGEN_CHOICES)
    proveedor = models.ForeignKey('proveedores.Proveedor')
    stock = models.IntegerField(default=1)
    ubicacion = models.ForeignKey('depositos.Ubicacion', null=True)
    
    def __unicode__(self):
        return self.nombre
    
    
class Vencimiento(models.Model):
    '''
    Este modelo representa un vencimiento.
    '''
    cantidad = models.IntegerField(default=1)
    vencimiento = models.DateField()
    producto = models.ForeignKey('Producto')
    
    def __unicode__(self):
        return self.vencimiento
    