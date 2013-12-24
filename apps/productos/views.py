from django.shortcuts import render_to_response
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.views.generic.edit import FormView
# from django.http import HttpResponse
# from django.utils import simplejson
# from django.core.exceptions import ObjectDoesNotExist


class Alta(FormView):
    template_name = 'productos/alta.html'
    

def alta(request): #deprecated
    return render_to_response('productos/alta.html', context_instance=RequestContext(request))


def edicion(request): #deprecated
    return render_to_response('productos/edicion.html', context_instance=RequestContext(request))


def baja(request): #deprecated
    return render_to_response('productos/baja.html', context_instance=RequestContext(request))
