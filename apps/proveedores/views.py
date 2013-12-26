from django.shortcuts import render_to_response
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.views.generic.edit import CreateView
#from django.views.generic.edit import FormView
# from django.http import HttpResponse
# from django.utils import simplejson
# from django.core.exceptions import ObjectDoesNotExist

from .models import Proveedor


class Alta(CreateView):
    template_name = 'proveedores/alta.html'
    model = Proveedor
    success_url = "/"
