from django.shortcuts import render_to_response
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
# from django.http import HttpResponse
# from django.utils import simplejson
# from django.core.exceptions import ObjectDoesNotExist

from .models import Proveedor


class Alta(CreateView):
    template_name = 'proveedores/alta.html'
    model = Proveedor
    success_url = "/"
    
    
class Listado(ListView):
    template_name = 'proveedores/listado.html'
    model = Proveedor
    
class Edicion(UpdateView):
    # form_class = PortfoliosCreateForm
    model = Proveedor
    template_name = 'proveedores/edicion.html'
    success_url = reverse_lazy('listado_proveedores')

    def get(self, request, **kwargs):
        self.object = Proveedor.objects.get(id=self.kwargs['id'])
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def get_object(self, queryset=None):
        obj = Proveedor.objects.get(id=self.kwargs['id'])
        return obj
