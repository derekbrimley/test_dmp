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
####SHOWS LIST OF ORDERS
@view_function
@permission_required('homepage.is_manager',login_url='/homepage/login/')
def process_request(request):
	params = {}
	
	orders = hmod.Order.objects.all()
	params['orders'] = orders
	
	return templater.render_to_response(request,'orders.html',params)

	
######################################################################
####EDITS SINGLE ORDER
@view_function
@permission_required('homepage.is_manager',login_url='/homepage/login/')
def edit(request):
	params = {}

	try:
		order = hmod.Order.objects.get(id=request.urlparams[0])
	except:
		return HttpResponseRedirect('/homepage/orders/')
		
	form = 	OrderEditForm(initial={
		'order_date': order.order_date,
		'date_packed':  order.date_packed,
		'date_paid': order.date_paid,
		'date_shipped': order.date_shipped,
		'tracking_number': order.tracking_number,
	})
		
	if request.method == 'POST':
		form = OrderEditForm(request.POST)
		if form.is_valid():
			order.date_packed = form.cleaned_data['order_date']
			order.date_paid = form.cleaned_data['date_paid']
			order.date_shipped = form.cleaned_data['date_shipped']
			order.tracking_number = form.cleaned_data['tracking_number']
			order.save()
			return HttpResponseRedirect('/homepage/orders/')
			
	params['form'] = form
	return templater.render_to_response(request,'orders.edit.html',params)
			
class OrderEditForm(forms.Form):
	order_date = forms.CharField(
		widget=forms.DateInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Order Date'
			}
		)
	)
	date_packed = forms.CharField(
		widget=forms.DateInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Date Packed'
			}
		)
	)
	date_paid = forms.CharField(
		widget=forms.DateInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Date Paid'
			}
		)
	)
	date_shipped = forms.CharField(
		widget=forms.DateInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Date Shipped'
			}
		)
	)
	tracking_number = forms.IntegerField(
		widget=forms.NumberInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Tracking Number'
			}
		)
	)	
		
######################################################################
####CREATES SINGLE ORDER
@view_function
@permission_required('homepage.is_manager',login_url='/homepage/login/')
def create(request):
	order = hmod.Order()
	order.order_date = '1111-1-1'
	order.date_packed = '1111-1-1'
	order.date_paid = '1111-1-1'
	order.date_shipped = '1111-1-1'
	order.tracking_number = '12345'
	order.save()
	
	return HttpResponseRedirect('/homepage/orders.edit/{}/'.format(order.id))
	
	
######################################################################
####DELETES SINGLE ORDER
@view_function
@permission_required('homepage.is_manager',login_url='/homepage/login/')
def delete(request):

	try:
		order = hmod.Order.objects.get(id=request.urlparams[0])
	except hmod.DoesNotExist:
		return HttpResponseRedirect('/homepage/orders/')
	
	order.delete()
	
	return HttpResponseRedirect('/homepage/orders/')
	
	
	