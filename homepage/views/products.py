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
#SHOWS LIST OF PRODUCTS
@view_function
def process_request(request):
	params = {}
	
	products = hmod.StockedProduct.objects.all()
	
	params['products'] = products
	return templater.render_to_response(request,'products.html',params)
	
######################################################################
#EDITS SINGLE PRODUCT
@view_function
@permission_required('homepage.is_manager',login_url='/homepage/login/')
def edit(request):
	params = {}
	
	try:
		product = hmod.StockedProduct.objects.get(id=request.urlparams[0])
	except hmod.StockedProduct.DoesNotExist:
		return HttpResponseRedirect('/homepage/products/')

	form = ProductEditForm(initial={
		'name': product.name,
		'quantity_on_hand': product.quantity_on_hand,
		'shelf_location': product.shelf_location,
		'order_file': product.order_file,
		'description': product.description,
		'manufacturer': product.manufacturer,
		'price': product.price,
		'sku': product.sku,
		'order_form_name': product.order_form_name,
		'production_time': product.production_time,
		'vendor_id': product.vendor_id,
		'category': product.category,
	})
	
	if request.method == 'POST':
		form = ProductEditForm(request.POST)
		if form.is_valid():
			product.name = form.cleaned_data['name']
			product.quantity_on_hand = form.cleaned_data['quantity_on_hand']
			product.shelf_location = form.cleaned_data['shelf_location']
			product.order_file = form.cleaned_data['order_file']
			product.description = form.cleaned_data['description']
			product.manufacturer = form.cleaned_data['manufacturer']
			product.price = form.cleaned_data['price']
			product.sku = form.cleaned_data['sku']
			product.order_form_name = form.cleaned_data['order_form_name']
			product.production_time = form.cleaned_data['production_time']
			product.vendor_id = form.cleaned_data['vendor_id']
			product.category = form.cleaned_data['category']
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
	quantity_on_hand = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Quantity on Hand'
			}
		)
	)
	shelf_location = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Shelf Location'
			}
		)
	)
	order_file = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Order File'
			}
		)
	)
	description = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Description'
			}
		)
	)
	manufacturer = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Manufacturer'
			}
		)
	)
	price = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Price'
			}
		)
	)
	sku = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'SKU'
			}
		)
	)
	order_form_name = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Order Form Name'
			}
		)
	)
	production_time = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Production Time'
			}
		)
	)
	vendor_id = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Vendor ID'
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
	
######################################################################
####CREATES SINGLE PRODUCT
@view_function
@permission_required('homepage.is_manager',login_url='/homepage/login/')
def create(request):

	product = hmod.RentalProduct()
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
		product = hmod.RentalProduct.objects.get(id=request.urlparams[0])
	except hmod.DoesNotExist:
		return HttpResponseRedirect('/homepage/products/')
	
	product.delete()
	return HttpResponseRedirect('/homepage/products/')
	
	
	
	
	
	
	
	