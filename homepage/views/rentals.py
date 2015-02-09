from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.utils import timezone
from django.contrib.auth.decorators import permission_required

templater = get_renderer('homepage')

#####################################################################
####GETS ALL RENTALS
@view_function
@permission_required('homepage.is_manager',login_url='/homepage/login/')
def process_request(request):
	params = {}
	
	rentals = hmod.Rental.objects.all()
	params['rentals'] = rentals
	
	return templater.render_to_response(request,'rentals.html',params)
	

#####################################################################
####EDITS SINGLE RENTAL
@view_function
@permission_required('homepage.is_manager',login_url='/homepage/login/')
def edit(request):
	params = {}
	
	try:
		rental = hmod.Rental.objects.get(id=request.urlparams[0])
	except:
		return HttpResponseRedirect('/homepage/rentals/')
	
	form = RentalEditForm(initial={
		'rental_time': rental.rental_time,
		'due_date': rental.due_date,
		'discount_percent': rental.discount_percent,
	})
	
	if request.method == "POST":
		form = RentalEditForm(request.POST)
		if form.is_valid():
			rental.rental_time = form.cleaned_data['rental_time']
			rental.due_date = form.cleaned_data['due_date']
			rental.discount_percent = form.cleaned_data['discount_percent']
			rental.save()
			return HttpResponseRedirect('/homepage/rentals/')
	
	params['form'] = form
	
	return templater.render_to_response(request,'rentals.edit.html',params)
	
class RentalEditForm(forms.Form):
	rental_time = forms.CharField(
		widget=forms.DateTimeInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Rental Time'
			}
		)
	)
	due_date = forms.CharField(
		widget=forms.DateTimeInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Due Date'
			}
		)
	)
	discount_percent = forms.DecimalField(
		required=True,
		min_value=.001,
		max_value=1,
		widget=forms.NumberInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Discount Percent'
			}
		)
	)

	
#####################################################################
####CREATES SINGLE RENTAL
@view_function
@permission_required('homepage.is_manager',login_url='/homepage/login/')
def create(request):
	
	rental = hmod.Rental()
	rental.rental_time = '1111-1-1'
	rental.due_date = '1111-1-1'
	rental.discount_percent = '0'
	rental.save()
	
	return HttpResponseRedirect('/homepage/rentals.edit/{}/'.format(rental.id))
	
	
#####################################################################
####DELETES SINGLE RENTAL	
@view_function
@permission_required('homepage.is_manager',login_url='/homepage/login/')
def delete(request):

	try:
		rental = hmod.Rental.objects.get(id=request.urlparams[0])
	except hmod.DoesNotExist:
		return HttpResponseRedirect('/homepage/rentals/')
	
	rental.delete()
	
	return HttpResponseRedirect('/homepage/rentals/')
	







