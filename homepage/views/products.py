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
####SHOWS LIST OF PRODUCTS
@view_function
def process_request(request):
	params = {}
	
	products = hmod.Product.objects.all()
	params['products'] = products
	
	return templater.render_to_response(request,'products.html',params)
	
	
######################################################################
####EDITS SINGLE PRODUCT
@view_function
@permission_required('homepage.is_manager',login_url='/homepage/login/')
def edit(request):
	params = {}
	
	try:
		product = hmod.Product.objects.get(id=request.urlparams[0])
	except hmod.Product.DoesNotExist:
		return HttpResponseRedirect('/homepage/products/')

	form = ProductEditForm(initial={
		'name': product.name,
		'description': product.description,
		'category': product.category,
		'current_price': product.current_price,
	})
	
	if request.method == 'POST':
		form = ProductEditForm(request.POST)
		if form.is_valid():
			product.name = form.cleaned_data['name']
			product.description = form.cleaned_data['description']
			product.category = form.cleaned_data['category']
			product.current_price = form.cleaned_data['current_price']
			product.save()
			return HttpResponseRedirect('/homepage/products/')
			
	params['form'] = form
	return templater.render_to_response(request,'products.edit.html',params)
	
class ProductEditForm(forms.Form):
	name = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Name'
			}
		)
	)
	description = forms.CharField(
		widget=forms.Textarea(
			attrs={
				'class': 'form-control',
				'placeholder': 'Description'
			}
		)
	)
	category = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Category'
			}
		)
	)
	current_price = forms.DecimalField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Price'
			}
		)
	)
	
######################################################################
####CREATES SINGLE PRODUCT
@view_function
@permission_required('homepage.is_manager',login_url='/homepage/login/')
def create(request):

	product = hmod.Product()
	product.name = ''
	product.description = ''
	product.category = ''
	product.current_price = '0'
	product.save()
	
	return HttpResponseRedirect('/homepage/products.edit/{}/'.format(product.id))
	
	
######################################################################
####DELETS SINGLE PRODUCT
@view_function
@permission_required('homepage.is_manager',login_url='/homepage/login/')
def delete(request):
	try:
		product = hmod.Product.objects.get(id=request.urlparams[0])
	except hmod.DoesNotExist:
		return HttpResponseRedirect('/homepage/products/')
	
	product.delete()
	return HttpResponseRedirect('/homepage/products/')
	
	
	
	
	
	
	
	