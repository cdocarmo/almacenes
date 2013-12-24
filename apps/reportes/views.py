from django.shortcuts import render_to_response
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
# from django.http import HttpResponse
# from django.utils import simplejson
# from django.core.exceptions import ObjectDoesNotExist


def alta(request):
    return render_to_response('reportes/alta.html', context_instance=RequestContext(request))


def edicion(request):
    return render_to_response('reportes/edicion.html', context_instance=RequestContext(request))


def baja(request):
    return render_to_response('reportes/baja.html', context_instance=RequestContext(request))
