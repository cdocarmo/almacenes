from django.shortcuts import render_to_response
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.views.generic.edit import FormView, UpdateView
# from django.http import HttpResponse
# from django.utils import simplejson
# from django.core.exceptions import ObjectDoesNotExist

from .forms import AltaDeUsuario

class Alta(FormView):
    template_name = 'usuarios/alta.html'
    form_class = AltaDeUsuario
    success_url = '/'
    
    def form_valid(self, form):
        return Super(Alta, self).form_valid(form)

# def alta(request):
#     return render_to_response('usuarios/alta.html', context_instance=RequestContext(request))

class Edicion(UpdateView):
    pass


#def edicion(request):
#    return render_to_response('usuarios/edicion.html', context_instance=RequestContext(request))


def baja(request):
    return render_to_response('usuarios/baja.html', context_instance=RequestContext(request))
