from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.decorators import permission_required
 
templater = get_renderer('account')

######################################################################
### SHOWS THE LIST OF USERS
@view_function
@permission_required('homepage.is_manager', login_url='/account/login/')
def process_request(request):
	params = {}
	
	users = hmod.User.objects.all()
	params['users'] = users
	
	return templater.render_to_response(request,'users.html',params)
	
######################################################################
###EDITS A SINGLE USER
@view_function
def edit(request):
	params = {}
	
	try:
		user = hmod.User.objects.get(id=request.urlparams[0])
	except hmod.User.DoesNotExist:
		return HttpResponseRedirect('/account/users/')
		
	user_id = user.id
	user_address = user.address.id
	
	try:
		address = hmod.Address.objects.get(id=user_address)
	except hmod.Address.DoesNotExist:
		return HttpResponseRedirect('/account/users/')
		
		
	form = UserEditForm(initial={
        'username':  user.username,
        'password':  user.password,
        'first_name':  user.first_name,
        'last_name':  user.last_name,
        'email':  user.email,
		'security_question': user.security_question,
		'security_answer': user.security_answer,
		'phone': user.phone,
        'address': address.address1,
        'city': address.city,
        'state': address.state,
        'zip': address.zip
    })
	
	if request.method == 'POST':
		form = UserEditForm(request.POST)
		form.userid = user.id
		if form.is_valid():
			user.username = form.cleaned_data['username']
			user.set_password(form.cleaned_data['password'])
			user.first_name = form.cleaned_data['first_name']
			user.last_name = form.cleaned_data['last_name']
			user.email = form.cleaned_data['email']
			user.security_question = form.cleaned_data['security_question']
			user.security_answer = form.cleaned_data['security_answer']
			user.phone = form.cleaned_data['phone']
			address.address1 = form.cleaned_data['address']
			address.city = form.cleaned_data['city']
			address.state = form.cleaned_data['state']
			address.zip = form.cleaned_data['zip']
			user.save()
			address.save()
			
			current_user = request.user
			return HttpResponseRedirect('/account/users/')
		
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
	address = forms.CharField(required=True, min_length=1, max_length=100)
	city = forms.CharField(required=True, min_length=1, max_length=100)
	state = forms.CharField(required=True, min_length=1, max_length=100)
	zip = forms.IntegerField()

	# def clean_username(self):
		# user_count = hmod.User.objects.filter(username=self.cleaned_data['username]).exclude(id=self.userid).count()
		# if len(users) >= 1:
			# raise forms.ValidationError("This username is already taken.")
		# return self.cleaned_data['username']
	

######################################################################
###CREATES A SINGLE USER
@view_function
def create(request):
	user = hmod.User()
	address = hmod.Address()
	
	address.address = ''
	address.city = ''
	address.state = ''
	address.zip = ''
	address.save()

	address_id = address.id

	user.password = ''
	user.last_login = '2012-12-12 12:12'
	user.is_superuser = 'false'
	user.username = ''
	user.security_question = ''
	user.security_answer = ''
	user.first_name = ''
	user.last_name = ''
	user.email_name = ''
	user.phone = ''
	user.is_staff = 'false'
	user.is_active = 'false'
	user.date_joined = '2012-12-12 12:12'
	user.address_id = address_id

	user.save()
	
	return HttpResponseRedirect('/account/users.edit/{}/'.format(user.id))
	
	
######################################################################
###DELETES A USER
@view_function
@permission_required('homepage.is_admin',login_url='/account/login/')
def delete(request):
	try:
		user = hmod.User.objects.get(id=request.urlparams[0])
	except hmod.DoesNotExist:
		return HttpResponseRedirect('/account/users/')
	
	user.delete()
	return HttpResponseRedirect('/account/users/')
	
	