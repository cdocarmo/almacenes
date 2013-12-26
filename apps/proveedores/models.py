from django.db import models


class Proveedor(models.Model):
    nombre = models.CharField(max_length=24)
    telefono1 = models.CharField(max_length=8)
    telefono2 = models.CharField(max_length=8, null=True)
    telefono3 = models.CharField(max_length=8, null=True)
    celular = models.CharField(max_length=9, null=True)
    domicilio = models.CharField(max_length=24, null=True)
