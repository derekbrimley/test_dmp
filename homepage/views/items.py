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
def process_request(request):
	params = {}
	
	items = hmod.Item.objects.all()
	specs = hmod.ProductSpecification.objects.all()
	
	params['items'] = items
	#params['specs'] = specs
	return templater.render_to_response(request,'items.html',params)
	
######################################################################
####EDITS SINGLE ITEM
@view_function
@permission_required('homepage.is_manager',login_url='/homepage/login/')
def edit(request):
	params = {}
	
	try:
		item = hmod.Item.objects.get(id=request.urlparams[0])
	except hmod.Item.DoesNotExist:
		return HttpResponseRedirect('/homepage/items/')

	form = ItemEditForm(initial={
		'quantity_on_hand': item.quantity_on_hand,
		'shelf_location': item.shelf_location,
		'order_file': item.order_file,
		'serial_number': item.serial_number,
		'date_acquired': item.date_acquired,
		'cost': item.cost,
		'status': item.status,
		'for_sale': item.for_sale,
		'condition_new': item.condition_new,
		'is_rentable': item.is_rentable,
		'notes': item.notes,
		'size': item.size,
		'size_modifier': item.size_modifier,
		'gender': item.gender,
		'color': item.color,
		'pattern': item.pattern,
		'start_year': item.start_year,
		'end_year': item.end_year,
		'note': item.note,
		'times_rented': item.times_rented,
		'price_per_day': item.price_per_day,
		'replacement_price': item.replacement_price,

	})
	
	if request.method == 'POST':
		form = ItemEditForm(request.POST)
		if form.is_valid():
			item.quantity_on_hand = form.cleaned_data['quantity_on_hand']
			item.shelf_location = form.cleaned_data['shelf_location']
			item.order_file = form.cleaned_data['order_file']
			item.serial_number = form.cleaned_data['serial_number']
			item.date_acquired = form.cleaned_data['date_acquired']
			item.cost = form.cleaned_data['cost']
			item.status = form.cleaned_data['status']
			item.for_sale = form.cleaned_data['for_sale']
			item.condition_new = form.cleaned_data['condition_new']
			item.is_rentable = form.cleaned_data['is_rentable']
			item.notes = form.cleaned_data['notes']
			item.size = form.cleaned_data['size']
			item.size_modifier = form.cleaned_data['size_modifier']
			item.gender = form.cleaned_data['gender']
			item.color = form.cleaned_data['color']
			item.pattern = form.cleaned_data['pattern']
			item.start_year = form.cleaned_data['start_year']
			item.end_year = form.cleaned_data['end_year']
			item.note = form.cleaned_data['note']
			item.times_rented = form.cleaned_data['times_rented']
			item.price_per_day = form.cleaned_data['price_per_day']
			item.replacement_price = form.cleaned_data['replacement_price']
			item.save()
			return HttpResponseRedirect('/homepage/items/')
	
	params['form'] = form
	return templater.render_to_response(request,'items.edit.html',params)
	
class ItemEditForm(forms.Form):
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
	serial_number = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Serial Number'
			}
		)
	)
	date_acquired = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Date Acquired'
			}
		)
	)
	cost = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Cost'
			}
		)
	)
	status = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Status'
			}
		)
	)
	for_sale = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'For Sale'
			}
		)
	)
	condition_new = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Condition New'
			}
		)
	)
	is_rentable = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Is Rentable'
			}
		)
	)
	notes = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Notes'
			}
		)
	)
	size = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Size'
			}
		)
	)
	size_modifier = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Size Modifier'
			}
		)
	)
	gender = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Gender'
			}
		)
	)
	color = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Color'
			}
		)
	)
	pattern = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Pattern'
			}
		)
	)
	start_year = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Start Year'
			}
		)
	)
	end_year = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'End Year'
			}
		)
	)
	note = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Note'
			}
		)
	)
	times_rented = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Times Rented'
			}
		)
	)
	price_per_day = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Price Per Day'
			}
		)
	)
	replacement_price = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Replacement Price'
			}
		)
	)
	
	
######################################################################
####CREATES SINGLE ITEM
@view_function
@permission_required('homepage.is_manager',login_url='/homepage/login/')
def create(request):

	item = hmod.Item()
	item.quantity_on_hand = '0'
	item.shelf_location = ''
	item.order_file = '0'
	item.serial_number = '0'
	item.date_acquired = '2015-01-01'
	item.cost = '0.0'
	item.notes = ''
	item.size = '0.0'
	item.size_modifier = '0.0'
	item.gender = ''
	item.color = ''
	item.pattern = ''
	item.start_year = '0'
	item.end_year = '0'
	item.note = ''
	item.times_rented = '0'
	item.price_per_day = '0.0'
	item.replacement_price = '0.0'

	item.save()
	
	return HttpResponseRedirect('/homepage/items.edit/{}/'.format(item.id))
	
	
######################################################################
####DELETS SINGLE ITEM
@view_function
@permission_required('homepage.is_manager',login_url='/homepage/login/')
def delete(request):
	try:
		item = hmod.Item.objects.get(id=request.urlparams[0])
	except hmod.DoesNotExist:
		return HttpResponseRedirect('/homepage/items/')
	
	item.delete()
	return HttpResponseRedirect('/homepage/items/')
	
	
	
	
	
	
	
	