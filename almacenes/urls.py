from django.conf.urls import patterns, include, url

from apps.usuarios.views import Alta as AltaUsuario
from apps.depositos.views import Alta as AltaDeposito
from apps.productos.views import Alta as AltaProducto
from apps.proveedores.views import Alta as AltaProveedor
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    #INDEX
    url(r'^$', 'apps.depositos.views.index', name='index'),
    #USUARIOS
    url(r'^usuarios/alta/$', AltaUsuario.as_view(), name='alta_usuario'),
    url(r'^usuarios/edicion/$', 'apps.usuarios.views.edicion', name='edicion_usuario'),
    url(r'^usuarios/baja/$', 'apps.usuarios.views.baja', name='baja_usuario'),
    #PRODUCTOS
    url(r'^productos/alta/$', AltaProducto.as_view(), name='alta_producto'),
    url(r'^productos/edicion/$', 'apps.productos.views.edicion', name='edicion_producto'),
    url(r'^productos/baja/$', 'apps.productos.views.baja', name='baja_producto'),
    #PROVEEDORES
    url(r'^proveedores/alta/$', AltaProveedor.as_view(), name='alta_producto'),
    # url(r'^proveedores/edicion/$', '' , name='edicion_producto'),
    # url(r'^proveedores/baja/$', '', name='baja_producto'),
    #DEPOSITOS
    url(r'^depositos/alta/$', AltaDeposito.as_view(), name='alta_deposito'),
    url(r'^depositos/edicion/$', 'apps.depositos.views.edicion', name='edicion_deposito'),
    url(r'^depositos/baja/$', 'apps.depositos.views.baja', name='baja_deposito'),
    #REPORTES
    url(r'^reportes/listado-de-usuarios/$', 'apps.usuarios.views.listadoDeUsuarios', name='listado_usuarios'),
    url(r'^reportes/listado-de-productos/$', 'apps.usuarios.views.listadoDeProductos', name='listado_productos'),
    url(r'^reportes/listado-de-depositos/$', 'apps.usuarios.views.listadoDeDepositos', name='listado_depositos'),
    # Examples:
    # url(r'^$', 'almacenes.views.home', name='home'),
    # url(r'^almacenes/', include('almacenes.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
