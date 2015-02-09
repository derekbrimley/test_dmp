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
####SHOWS LIST OF ITEMS
@view_function
@permission_required('homepage.is_manager', login_url='/homepage/login/')
def process_request(request):
	params = {}
	
	items = hmod.Item.objects.all()
	params['items'] = items
	
	return templater.render_to_response(request,'items.html',params)
	
#######################################################################
####EDITS A SINGLE ITEM
@view_function
@permission_required('homepage.is_manager',login_url='/homepage/login/')
def edit(request):
	params = {}
	
	try:
		item = hmod.Item.objects.get(id=request.urlparams[0])
	except hmod.Item.DoesNotExist:
		return HttpResponseRedirect('/homepage/items/')
		
	form = ItemEditForm(initial=
		{
			'name': item.name,
			'description': item.description,
			'value': item.value,
			'rental_price': item.standard_rental_price,
			'rentable': item.rentable,
		}
	)
	
	if request.method == "POST":
		form = ItemEditForm(request.POST)
		if form.is_valid():
			item.name = form.cleaned_data['name']
			item.description = form.cleaned_data['description']
			item.value = form.cleaned_data['value']
			item.rentable = form.cleaned_data['rentable']
			item.standard_rental_price = form.cleaned_data['rental_price']
			item.save()
			return HttpResponseRedirect('/homepage/items/')
	
	params['form'] = form
	
	return templater.render_to_response(request,'items.edit.html',params)
	
class ItemEditForm(forms.Form):
	name = forms.CharField(
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Name'
			}
		)
	)
	description = forms.CharField(
		required=True,
		min_length=1,
		max_length=500,
		widget=forms.Textarea(
			attrs={
				'class': 'form-control',
				'placeholder': 'Description'
			}
		)
	)
	value = forms.DecimalField(
		required=True,
		min_value=.01,
		max_value=10000,
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Value'
			}
		)
	)
	rental_price = forms.DecimalField(
		required=True,
		min_value=.01,
		max_value=10000,
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Rental Price'
			}
		)
	)
	rentable = forms.BooleanField(
		required=False,
		widget=forms.NullBooleanSelect(
			attrs={
				'class': 'form-control'
			}
		)
	)

	
#######################################################################
####DELETES A SINGLE ITEM	
@view_function
@permission_required('homepage.is_manager',login_url='/homepage/login/')
def create(request):
	params = {}
	
	item = hmod.Item()
	item.name = ''
	item.description = ''
	item.value = '0'
	item.standard_rental_price = '0'
	item.rentable = ''
	item.save()
	
	return HttpResponseRedirect('/homepage/items.edit/{}/'.format(item.id))
	
#######################################################################
####DELETES A SINGLE ITEM	
@view_function
@permission_required('homepage.is_manager',login_url='/homepage/login/')
def delete(request):
	params = {}
	
	item = hmod.Item.objects.get(id=request.urlparams[0])

	item.delete()
	
	return HttpResponseRedirect('/homepage/items/')
	
	