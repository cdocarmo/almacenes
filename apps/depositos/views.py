from django.shortcuts import render_to_response
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
# from django.http import HttpResponse
# from django.utils import simplejson
# from django.core.exceptions import ObjectDoesNotExist


def index(request):
    # VISTA TEMPORAL
    return render_to_response('index.html', context_instance=RequestContext(request))


def alta(request):
    return render_to_response('depositos/alta.html', context_instance=RequestContext(request))


def edicion(request):
    return render_to_response('depositos/edicion.html', context_instance=RequestContext(request))


def baja(request):
    return render_to_response('depositos/baja.html', context_instance=RequestContext(request))
