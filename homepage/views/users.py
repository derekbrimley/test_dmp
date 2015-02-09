from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.decorators import permission_required

 
templater = get_renderer('homepage')

######################################################################
### SHOWS THE LIST OF USERS
@view_function
@permission_required('homepage.is_manager', login_url='/homepage/login/')
def process_request(request):
	params = {}
	
	users = hmod.User.objects.all()
	params['users'] = users
	
	return templater.render_to_response(request,'users.html',params)
	
######################################################################
###EDITS A SINGLE USER
@view_function
@permission_required('homepage.is_admin',login_url='/homepage/login/')
def edit(request):
	params = {}
	
	try:
		user = hmod.User.objects.get(id=request.urlparams[0])
	except hmod.User.DoesNotExist:
		return HttpResponseRedirect('/homepage/users/')
		
	form = UserEditForm(initial={
		'username': user.username,
		'password': user.password,
		'email': user.email,
		'first_name': user.first_name,
		'last_name': user.last_name,
		'address': user.address,
		'city': user.city,
		'state': user.state,
		'zip': user.zip,
	})
	
	if request.method == 'POST':
		form = UserEditForm(request.POST)
		form.userid = user.id
		if form.is_valid():
			user.username = form.cleaned_data['username']
			user.set_password(form.cleaned_data['password'])
			user.email = form.cleaned_data['email']
			user.first_name = form.cleaned_data['first_name']
			user.last_name = form.cleaned_data['last_name']
			user.address = form.cleaned_data['address']
			user.city = form.cleaned_data['city']
			user.state = form.cleaned_data['state']
			user.zip = form.cleaned_data['zip']
			user.save()
			return HttpResponseRedirect('/homepage/users/')
		
	params['form'] = form
	return templater.render_to_response(request,'users.edit.html',params)
	
	
class UserEditForm(forms.Form):
	first_name = forms.CharField(
		required=True,
		min_length=1,
		max_length=100,
		label = 'First Name',
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'First Name'
			}
		)
	)
	last_name = forms.CharField(
		required=True,
		min_length=1,
		max_length=100,
		label = 'Last Name',
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Last Name'
			}
		)
	)
	email = forms.EmailField(
		required=True,
		min_length=1,
		max_length=100,
		label = 'Email',
		widget=forms.EmailInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Email'
			}
		)
	)
	username = forms.CharField(
		required=True,
		min_length=1,
		max_length=100,
		label = 'Username',
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Username'
			}
		)
	)
	password = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Password'
			}
		),
		label = 'Password',
	)
	address = forms.CharField(
		required=True,
		min_length=1,
		max_length=100,
		label = 'Address',
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Address'
			}
		)
	)
	city = forms.CharField(
		required=True,
		min_length=1,
		max_length=100,
		label = 'City',
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'City'
			}
		)
	)
	state = forms.CharField(
		required=True,
		min_length=1,
		max_length=100,
		label = 'State',
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'State'
			}
		)
	)
	zip = forms.CharField(
		required=True,
		min_length=1,
		max_length=100,
		label = 'Zip Code',
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Zip Code'
			}
		)
	)

	# def clean_username(self):
		# user_count = hmod.User.objects.filter(username=self.cleaned_data['username]).exclude(id=self.userid).count()
		# if len(users) >= 1:
			# raise forms.ValidationError("This username is already taken.")
		# return self.cleaned_data['username']
	

######################################################################
###CREATES A SINGLE USER
@view_function
@permission_required('homepage.is_admin',login_url='/homepage/login/')
def create(request):
	user = hmod.User()
	user.username = ''
	user.password = ''
	user.first_name = ''
	user.last_name = ''
	user.email = ''
	user.is_staff = ''
	user.is_active = True
	user.address = ''
	user.city = ''
	user.state = ''
	user.zip = '00000'
	user.save()
	
	return HttpResponseRedirect('/homepage/users.edit/{}/'.format(user.id))
	
	
######################################################################
###DELETES A USER
@view_function
@permission_required('homepage.is_admin',login_url='/homepage/login/')
def delete(request):
	try:
		user = hmod.User.objects.get(id=request.urlparams[0])
	except hmod.DoesNotExist:
		return HttpResponseRedirect('/homepage/users/')
	
	user.delete()
	return HttpResponseRedirect('/homepage/users/')
	
	
	
	
	