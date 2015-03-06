from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth import authenticate, login, logout

templater = get_renderer('account')

######################################################################
####LOGIN PAGE
@view_function
def process_request(request):
	params = {}
	
	form = UserLoginForm()
	
	if request.method == "POST":
		print("post")
		form = UserLoginForm(request.POST)
		
		username=request.POST['username']
		password=request.POST['password']
		
		if form.is_valid():
			try:
				user = authenticate(username=username,password=password)
				
				print("username: %s" %username)
				print("password: %s" %password)
			except:
				params['form'] = form
				return templater.render_to_response(request, 'login.login_form.html', params)
			if user is not None:
				if user.is_active:
					login(request,user)
					print("User is authenticated.")
					return HttpResponse('''
						<script>
							window.location.href = "/account/";
						</script>
					''')
				else:
					print("Account has been disabled.")
			else:
				print("User does not exist.")
		else:
			return templater.render_to_response(request,'login.login_form.html',params)
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

######################################################################
####CHECK USERNAME
@view_function
def check_username(request):

	username = request.REQUEST.get('u')
	
	# print('>>>>>>>>>>>>>',username)
	try:
		user = hmod.User.objects.get(username=username)
		return HttpResponse("0")
	except:
		return HttpResponse("1")


######################################################################
####LOGIN PAGE
@view_function
def login_form(request):
	params = {}
	
	form = UserLoginForm()
	
	if request.method == "POST":
		
		form = UserLoginForm(request.POST)
		
		username=request.POST['username']
		password=request.POST['password']
		
		if form.is_valid():
			try:
				user = authenticate(username=username,password=password)
				
				print("username: %s" %username)
				print("password: %s" %password)
				login(request,user)
				return HttpResponse('''
						<script>
							window.location.href = "/account/";
						</script>
					''')
			except:
				params['form'] = form
				return templater.render_to_response(request, 'login.login_form.html', params)
		else:
			print("form not valid")
			
	params['form'] = form
	
	return templater.render_to_response(request,'login.login_form.html',params)
