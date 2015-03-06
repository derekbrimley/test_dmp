from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django_mako_plus.controller import view_function

######################################################################
####LOGOUT PAGE
@view_function
def process_request(request):
	logout(request)
	
	return HttpResponseRedirect('/homepage/')
