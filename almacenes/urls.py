from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    #USUARIOS
    url(r'^usuarios/alta/$', 'usuarios.views.alta', name='alta_usuario'),
    url(r'^usuarios/edicion/$', 'usuarios.views.edicion', name='edicion_usuario'),
    url(r'^usuarios/baja/$', 'usuarios.views.baja', name='baja_usuario'),
    #PRODUCTOS
    url(r'^productos/alta/$', 'productos.views.alta', name='alta_producto'),
    url(r'^productos/edicion/$', 'productos.views.edicion', name='edicion_producto'),
    url(r'^productos/baja/$', 'productos.views.baja', name='baja_producto'),
    #DEPOSITOS
    url(r'^depositos/alta/$', 'depositos.views.alta', name='alta_deposito'),
    url(r'^depositos/edicion/$', 'depositos.views.edicion', name='edicion_deposito'),
    url(r'^depositos/baja/$', 'depositos.views.baja', name='baja_deposito'),
    #REPORTES
    url(r'^reportes/listado-de-usuarios/$', 'usuarios.views.listadoDeUsuarios', name='listado_usuarios'),
    url(r'^reportes/listado-de-productos/$', 'usuarios.views.listadoDeProductos', name='listado_productos'),
    url(r'^reportes/listado-de-depositos/$', 'usuarios.views.listadoDeDepositos', name='listado_depositos'),
    # Examples:
    # url(r'^$', 'almacenes.views.home', name='home'),
    # url(r'^almacenes/', include('almacenes.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
