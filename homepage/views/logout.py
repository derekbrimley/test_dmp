from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django.contrib.auth import logout
from django_mako_plus.controller import view_function

@view_function
def process_request(request):
	logout(request)
	
	return HttpResponseRedirect('/homepage/')
	