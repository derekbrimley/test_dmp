from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth import authenticate, login, logout

templater = get_renderer('homepage')

######################################################################
####LOGIN PAGE
@view_function
def process_request(request):
	params = {}
	
	form = UserLoginForm()
	
	if request.method == "POST":
		username=request.POST['username']
		password=request.POST['password']
		user = authenticate(username=username,password=password)
		print("username: %s" %username)
		print("password: %s" %password)
		if user is not None:
			if user.is_active:
				login(request,user)
				print("User is authenticated.")
				return HttpResponseRedirect('/homepage/')
			else:
				print("Account has been disabled.")
		else:
			print("User does not exist.")
		
	params['form'] = form
	
	return templater.render_to_response(request,'login.html',params)
	
class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	
######################################################################
####LOGOUT PAGE
@view_function
def logout(request):
	logout(request)
	
	return HttpResponseRedirect('/homepage/')








