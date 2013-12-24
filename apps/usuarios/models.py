from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PerfilDeUsuario(models.Model):
    usuario = models.OneToOneField(User)
    telefono = models.CharField(max_length=8)
    celular = models.CharField(max_length=9)
    domicilio = models.CharField(max_length=64)
    
    def __unicode__(self):
        return u'Perfil de Usuario: %s' % self.usuario.username
    
