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
####GETS ALL TRANSACTIONS
@view_function
@permission_required('homepage.is_manager',login_url='/homepage/login/')
def process_request(request):
	params = {}
	
	transactions = hmod.Transaction.objects.all()
	params['transactions'] = transactions
	
	return templater.render_to_response(request,'transactions.html',params)
	

#####################################################################
####EDITS SINGLE TRANSACTION
@view_function
@permission_required('homepage.is_manager',login_url='/homepage/login/')
def edit(request):
	params = {}
	
	try:
		transaction = hmod.Transaction.objects.get(id=request.urlparams[0])
	except:
		return HttpResponseRedirect('/homepage/transactions/')
	
	form = TransactionEditForm(initial={
		'date': transaction.date,
		'customer': transaction.customer,
		'date_packed': transaction.date_packed,
		'packed_by': transaction.packed_by,
		'date_paid': transaction.date_paid,
		'payment_handler': transaction.payment_handler,
		'date_shipped': transaction.date_shipped,
		'shipped_by': transaction.shipped_by,
		'tracking_number': transaction.tracking_number,
		'ships_to': transaction.ships_to,
		'packed_by': transaction.packed_by,
		'payment_processed_by': transaction.payment_processed_by,
		'shipped_by': transaction.shipped_by,
		'handled_by': transaction.handled_by,
	})
	
	if request.method == "POST":
		form = TransactionEditForm(request.POST)
		if form.is_valid():
			transaction.date = form.cleaned_data['date']
			transaction.customer = form.cleaned_data['customer']
			transaction.date_packed = form.cleaned_data['date_packed']
			transaction.packed_by = form.cleaned_data['packed_by']
			transaction.date_paid = form.cleaned_data['date_paid']
			transaction.payment_handler = form.cleaned_data['payment_handler']
			transaction.date_shipped = form.cleaned_data['date_shipped']
			transaction.shipped_by = form.cleaned_data['shipped_by']
			transaction.tracking_number = form.cleaned_data['tracking_number']
			transaction.ships_to = form.cleaned_data['ships_to']
			transaction.packed_by = form.cleaned_data['packed_by']
			transaction.payment_processed_by = form.cleaned_data['payment_processed_by']
			transaction.shipped_by = form.cleaned_data['shipped_by']
			transaction.handled_by = form.cleaned_data['handled_by']
			transaction.save()
			return HttpResponseRedirect('/homepage/transactions/')
	
	params['form'] = form
	
	return templater.render_to_response(request,'transactions.edit.html',params)
	
class TransactionEditForm(forms.Form):
	date = forms.CharField(
		widget=forms.DateTimeInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Date'
			}
		)
	)
	customer = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Customer'
			}
		)
	)
	date_packed = forms.CharField(
		required=True,
		widget=forms.DateTimeInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Date Packed'
			}
		)
	)
	packed_by = forms.CharField(
		required=True,
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Packed By'
			}
		)
	)
	date_paid = forms.CharField(
		required=True,
		widget=forms.DateTimeInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Date Paid'
			}
		)
	)
	payment_handler = forms.CharField(
		required=True,
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Payment Handler'
			}
		)
	)
	date_shipped = forms.CharField(
		required=True,
		widget=forms.DateTimeInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Date Shipped'
			}
		)
	)
	shipped_by = forms.CharField(
		required=True,
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Shipped By'
			}
		)
	)
	tracking_number = forms.CharField(
		required=True,
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Tracking Number'
			}
		)
	)
	ships_to = forms.CharField(
		required=True,
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Ships To'
			}
		)
	)
	packed_by = forms.CharField(
		required=True,
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Packed By'
			}
		)
	)
	payment_processed_by = forms.CharField(
		required=True,
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Payment Processed By'
			}
		)
	)
	shipped_by = forms.CharField(
		required=True,
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Shipped By'
			}
		)
	)
	handled_by = forms.CharField(
		required=True,
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Handled By'
			}
		)
	)

	
#####################################################################
####CREATES SINGLE TRANSACTIONS
@view_function
@permission_required('homepage.is_manager',login_url='/homepage/login/')
def create(request):
	
	transaction = hmod.Transaction()
	transaction.rental_time = '1111-1-1'
	transaction.due_date = '1111-1-1'
	transaction.discount_percent = '0'
	transaction.save()
	
	return HttpResponseRedirect('/homepage/transactions.edit/{}/'.format(transaction.id))
	
	
#####################################################################
####DELETES SINGLE TRANSACTIONS	
@view_function
@permission_required('homepage.is_manager',login_url='/homepage/login/')
def delete(request):

	try:
		transaction = hmod.Transaction.objects.get(id=request.urlparams[0])
	except hmod.DoesNotExist:
		return HttpResponseRedirect('/homepage/transactions/')
	
	transaction.delete()
	
	return HttpResponseRedirect('/homepage/transactions/')
	







