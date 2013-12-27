from django.db import models


class Proveedor(models.Model):
    nombre = models.CharField(max_length=24)
    telefono1 = models.CharField(max_length=8, unique=True)
    telefono2 = models.CharField(max_length=8, null=True)
    telefono3 = models.CharField(max_length=8, null=True)
    celular = models.CharField(max_length=9, null=True)
    domicilio = models.CharField(max_length=24, null=True)
    
    def __unicode__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('detalle_proveedor', kwargs={'pk': self.pk})
