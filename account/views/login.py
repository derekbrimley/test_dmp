from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth import authenticate, login, logout
from ldap3 import 	Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO

templater = get_renderer('account')

#######################################################
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
	
########################################################
####LOGOUT PAGE
@view_function
def logout(request):
	logout(request)
	
	return HttpResponseRedirect('/homepage/')

########################################################
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


########################################################
####LOGIN PAGE
@view_function
def login_form(request):
	params = {}
	
	form = UserLoginForm()
	
	if request.method == "POST":
		
		form = UserLoginForm(request.POST)
		
		
		if form.is_valid():
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			s = Server('www.colonialheritage.space',port=8889,get_info=GET_ALL_INFO)
			c = Connection(s, auto_bind = True,client_strategy = STRATEGY_SYNC,
									user = username,password=password,
									authentication = AUTH_SIMPLE)
			print("Connection>>>>>>>>>>>>>",c)
			
			# return HttpResponse('''
						# <script>
							# window.location.href = "/account/";
						# </script>
					# ''')
			if c!= None:
				user = hmod.User.objects.get_or_create(username=username)
				
				print("USER>>>>>>>>>>>>>>",username)
				
				user.password = pw
				user.last_login = '2012-12-12 12:12'
				user.is_superuser = 'false'
				user.security_question = ''
				user.security_answer = ''
				user.first_name = c.first_name
				user.last_name = c.last_name
				user.set_password = password
				user.email_name = ''
				user.phone = ''
				user.is_staff = 'false'
				user.is_active = 'false'
				user.date_joined = '2012-12-12 12:12'
				user.address_id = 1

				user.save()	

				u2 = authenticate(username=username,password=password)
				login(request, u2)
			
			else:
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

	
##########################################################
####LDAP LOGIN PAGE
@view_function
def ldap_login(request):
	params = {}
	
					
							
							
							