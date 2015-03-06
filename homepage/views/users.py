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
		'last_name': user.first_name,
		'security_question': user.security_question,
		'security_answer': user.security_answer,
		'phone': user.phone,
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
			user.security_question = form.cleaned_data['security_question']
			user.security_answer = form.cleaned_data['security_answer']
			user.phone = form.cleaned_data['phone']
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
	phone = forms.CharField(
		required=True,
		label = 'Username',
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Phone'
			}
		)
	)
	security_question = forms.CharField(
		required=True,
		min_length=1,
		max_length=200,
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Security Question'
			}
		)
	)
	security_answer = forms.CharField(
		required=True,
		min_length=1,
		max_length=200,
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Security Answer'
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
	organization_name = ''
	organization_type = ''
	security_question = ''
	security_answer = ''
	phone = ''
	requires_reset = ''
	date_appointed_agent = ''
	bio_sketch = ''
	relationship = ''
	emergency_contact = ''
	emergency_phone = ''
	emergency_relationship = ''
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
	
	