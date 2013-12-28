from django.shortcuts import render_to_response
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
# from django.http import HttpResponse
from django.http import HttpResponseRedirect
# from django.utils import simplejson
# from django.core.exceptions import ObjectDoesNotExist

from .forms import AltaDeDeposito, AltaDeUbicacion
from .models import Deposito

def index(request):
    # VISTA TEMPORAL
    return render_to_response('index.html', context_instance=RequestContext(request))


class Alta(CreateView):
    template_name = 'depositos/alta.html'
    model = Deposito
    form_class = AltaDeDeposito
    form_class_segundo = UbicacionFormSet
    success_url = '/'
    
    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form_ubicacion = form_class_segundo()
        return self.render_to_response(self.get_context_data(form=form, form_ubicacion=form_ubicacion))
    
    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ubicacion_form = form_class_segundo(self.request.POST)
        if (form.is_valid() and ubicacion_form.is_valid()):
            return self.form_valid(form, ubicacion_form)
        else:
            return self.form_invalid(form, ubicacion_form)
    
    def form_valid(self, form, ubicacion_form):
        self.object = form.save()
        ubicacion_form.instance = self.object
        ubicacion_form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form, ubicacion_form):
         return self.render_to_response(
            self.get_context_data(form=form,
                                  ubicacion_form=ubicacion_form))


class Listado(ListView):
    template_name = 'depositos/listado.html'
    model = Deposito
    

class Edicion(UpdateView):
    # form_class = PortfoliosCreateForm
    model = Deposito
    template_name = 'depositos/edicion.html'
    success_url = reverse_lazy('listado_depositos')

    def get(self, request, **kwargs):
        self.object = Deposito.objects.get(id=self.kwargs['id'])
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def get_object(self, queryset=None):
        obj = Deposito.objects.get(id=self.kwargs['id'])
        return obj
# def alta(request):
#    return render_to_response('depositos/alta.html', context_instance=RequestContext(request))


# def edicion(request):
#     return render_to_response('depositos/edicion.html', context_instance=RequestContext(request))


def baja(request):
    return render_to_response('depositos/baja.html', context_instance=RequestContext(request))
