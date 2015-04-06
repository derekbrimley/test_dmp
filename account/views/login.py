from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth import authenticate, login, logout
from ldap3 import 	Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO
from .. import dmp_render, dmp_render_to_response
from datetime import datetime

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

			try:

				username=form.cleaned_data['username']
				password=form.cleaned_data['password']
				s = Server('www.colonialheritage.space',port=8889,get_info=GET_ALL_INFO)
				c = Connection(s, auto_bind = True, client_strategy = STRATEGY_SYNC,
                               user= str(username) + '@colonialheritage.local',
                               password= str(password),authentication=AUTH_SIMPLE)
				print("Connection>>>>>>>>>>>>>",c)
				
				response = c.response
				print("RESPONSE:::::::::::",response)
				if response is None:
					
					search_results = c.search(
						search_base = 'CN=Users,DC=colonialheritage,DC=local',
						search_filter = '(samAccountName=' + username + ')',
						attributes = [
							'givenName',
							'sn',
							'userPrincipalName'
						]
					)
					
					user_info = c.response[0]['attributes']
					print("USER INFO::::::::::",user_info)
					
					first_name = user_info.get('givenName')
					last_name = user_info.get('sn')
					email = user_info.get('userPrincipalName')
					
					print("FIRST NAME:::::",first_name)
					print("LAST NAME::::::",last_name)
					print("EMAIL::::::::::::",email)
					address = hmod.Address()
		
					address.address = ''
					address.city = ''
					address.state = ''
					address.zip = ''
					address.save()

					address_id = address.id
					
					try:
						u = hmod.User.objects.get(username=username)
						print("USER ALREADY MADE")
						u.first_name = user_info.get('givenName')
						u.last_name = user_info.get('sn')
						u.email = user_info.get('userPrincipalName')
						u.username = username
						u.set_password(password)
						u.is_staff = True
						u.last_login = str(datetime.now())
						u.save()
						
					except:
						u = hmod.User()
						u.first_name = user_info.get('givenName')
						u.last_name = user_info.get('sn')
						u.email = user_info.get('userPrincipalName')
						u.username = username
						u.set_password(password)
						u.is_staff = True
						u.is_superuser = False
						u.last_login = str(datetime.now())
						print("USER NOT MADE")
						u.address_id = 1
						u.save()
						print("U:::::::::::",u)

					print("USER>>>>>>>>>>>>>>",username)
					
					u2 = authenticate(username=username,password=password)
					print("U2:::::::::::",u2)
					login(request, u2)
					return HttpResponse('''
								<script>
									window.location.href = "/account/";
								</script>
							''')
			except:
				try:
					user = authenticate(username=username,password=password)
					
					print("username: %s" %username)
					print("password: %s" %password)
					print("USER:::::::::::",user)
				except:
					params['form'] = form
					return templater.render_to_response(request, 'login.login_form.html', params)
				if user is not None:
					print('LOGGED IN')
					login(request,user)
					is_next = str(request.GET.get('next'))
					print(is_next)
					if is_next == 'None':
						return HttpResponse('''
							<script>
								window.location.href = "/account/";
							</script>
						''')
					else:
						return HttpResponseRedirect(request.GET.get('next'))
				else:
					params['form'] = form
					return dmp_render_to_response(request, 'login.login_form.html', params)
		else:
			print("form not valid")
			raise forms.ValidationError('User in not currently active')
			
	params['form'] = form
	
	return templater.render_to_response(request,'login.login_form.html',params)

	
##########################################################
####LDAP LOGIN PAGE
@view_function
def ldap_login(request):
	params = {}
	
					
							
							
							