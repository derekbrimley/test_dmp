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
####CREATE USER
@view_function
def process_request(request):
	params = {}
	
	form = UserEditForm(initial={
		'username' : user.username,
		'first_name': user.first_name,
		'last_name': user.last_name,
		'email' : user.email,
		'phone' : user.phone,
		'address1' : address.address1,
		'address2' : address.address2,
		'city' : address.city,
		'state' : address.state,
		'zip' : address.zip,
		'organization_name' : user.organization_name,
		'organization_type' : user.organization_type,
		'bio_sketch': user.bio_sketch,
		'emergency_contact': user.emergency_contact,
		'emergency_phone': user.emergency_phone,
		'emergency_relationship': user.emergency_relationship})

	if request.method == "POST":
		form = UserEditForm(request.POST)
		if form.is_valid():
			user.username = form.cleaned_data['username']
			user.first_name = form.cleaned_data['first_name']
			user.last_name = form.cleaned_data['last_name']
			user.email = form.cleaned_data['email']
			user.phone = form.cleaned_data['phone']
			address.address1 = form.cleaned_data['address1']
			address.address2 = form.cleaned_data['address2']
			address.city = form.cleaned_data['city']
			address.state = form.cleaned_data['state']
			address.zip = form.cleaned_data['zip']
			user.organization_name = form.cleaned_data['organization_name']
			user.organization_type = form.cleaned_data['organization_type']
			user.bio_sketch = form.cleaned_data['bio_sketch']
			user.emergency_contact = form.cleaned_data['emergency_contact']
			user.emergency_phone = form.cleaned_data['emergency_phone']
			user.emergency_relationship = form.cleaned_data['emergency_relationship']

			user.save()
            address.save()
	params['form'] = form
	
	return templater.render_to_response(request,'/account/login.html',params)
	
class UserEditForm(forms.Form):
	username = forms.CharField(label="Username", required=True, max_length=30)
	first_name = forms.CharField(label="First", required=True, max_length=100)
	last_name = forms.CharField(label="Last", required=True, max_length=100)
	email = forms.CharField(label="Email", required=True, max_length=100)
	phone = forms.CharField(label="Phone", required=True, max_length=100)
	address1 = forms.CharField(label="Address", required=True, max_length=100)
	address2 = forms.CharField(label="Address", required=True, max_length=100)
	city = forms.CharField(label='City', required=True, max_length=100)
	state = forms.CharField(label='State', required=True, max_length=100)
	zip = forms.CharField(label='Zip', required=True, max_length=100)
	organization_name = forms.CharField(label='Organization Name', required=False, max_length=100)
	organization_type = forms.CharField(label='Organization Type', required=False, max_length=100)
	bio_sketch = forms.CharField(label='Bio Sketch', required=False, max_length=200)
	emergency_contact = forms.CharField(label='Emergency Contact', required=False, max_length=100)
	emergency_phone = forms.CharField(label='Emergency Phone', required=False, max_length=14)
	emergency_relationship = forms.CharField(label='Emergency Relationship', required=False, max_length=100)
