from django.shortcuts import render_to_response
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
#from django.views.generic.edit import FormView
# from django.http import HttpResponse
# from django.utils import simplejson
# from django.core.exceptions import ObjectDoesNotExist

from .models import Producto


class Alta(CreateView):
    template_name = 'productos/alta.html'
    model = Producto
    success_url = "/"
    
    
class Listado(ListView):
    template_name = 'productos/listado.html'
    model = Producto
    
    
class Edicion(UpdateView):
    # form_class = PortfoliosCreateForm
    model = Producto
    template_name = 'productos/edicion.html'
    success_url = reverser_lazy('listado_productos')

    def get(self, request, **kwargs):
        self.object = Producto.objects.get(id=self.kwargs['id'])
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def get_object(self, queryset=None):
        obj = Producto.objects.get(id=self.kwargs['id'])
        return obj

#def alta(request): #deprecated
#    return render_to_response('productos/alta.html', context_instance=RequestContext(request))


#def edicion(request): #deprecated
#    return render_to_response('productos/edicion.html', context_instance=RequestContext(request))


def baja(request): #deprecated
    return render_to_response('productos/baja.html', context_instance=RequestContext(request))
