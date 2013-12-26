from django.shortcuts import render_to_response
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.views.generic.edit import CreateView
# from django.http import HttpResponse
from django.http import HttpResponseRedirect
# from django.utils import simplejson
# from django.core.exceptions import ObjectDoesNotExist

from .forms import AltaDeDeposito, UbicacionFormSet
from .models import Deposito

def index(request):
    # VISTA TEMPORAL
    return render_to_response('index.html', context_instance=RequestContext(request))


class Alta(CreateView):
    template_name = 'depositos/alta.html'
    model = Deposito
    form_class = AltaDeDeposito
    success_url = '/'
    
    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ubicacion_form = UbicacionFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ubicacion_form=ubicacion_form))
    
    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ubicacion_form = UbicacionFormSet(self.request.POST)
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

# def alta(request):
#    return render_to_response('depositos/alta.html', context_instance=RequestContext(request))


def edicion(request):
    return render_to_response('depositos/edicion.html', context_instance=RequestContext(request))


def baja(request):
    return render_to_response('depositos/baja.html', context_instance=RequestContext(request))
