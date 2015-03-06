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
	
	events = hmod.Event.objects.all()
	params['events'] = events
	
	return templater.render_to_response(request,'events.html',params)
	
######################################################################
####EDIT SINGLE EVENT
@view_function
@permission_required('homepage.is_manager',login_url='/homepage/login/')
def edit(request):
	params = {}
	
	try:
		event = hmod.Event.objects.get(id=request.urlparams[0])
	except:
	    return HttpResponseRedirect('/homepage/events/')
	
	form = EventEditForm(initial={
		'name': event.name,
		'description': event.description,
		'start_date': event.start_date,
		'end_date': event.end_date,
		'map_file': event.map_file,
		'venue_name': event.venue_name,
		'address': event.address,
	})
	
	if request.method == "POST":
		form = EventEditForm(request.POST)
		if form.is_valid():
			event.name = form.cleaned_data['name']
			event.description = form.cleaned_data['description']
			event.start_date = form.cleaned_data['start_date']
			event.end_date = form.cleaned_data['end_date']
			event.map_file = form.cleaned_data['map_file']
			event.venue_name = form.cleaned_data['map_file']
			event.address = form.cleaned_data['address']
			event.save()
			return HttpResponseRedirect('/homepage/events/')

	params['form'] = form
	
	return templater.render_to_response(request,'events.edit.html',params)

class EventEditForm(forms.Form):
	name = forms.CharField(
		required=True,
		label = 'Name',
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Name'
			}
		)
	)
	description = forms.CharField(
		required=True,
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Description'
			}
		)
	)
	start_date = forms.DateField(
		required=True,
		label = 'Start Date',
		widget=forms.DateInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Start Date'
			}
		)
	)
	end_date = forms.DateField(
		required=True,
		label = 'End Date',
		widget=forms.DateInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'End Date'
			}
		)
	)
	map_file = forms.CharField(
		required=True,
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Map File'
			}
		)
	)
	venue_name = forms.CharField(
		required=True,
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Venue Name'
			}
		)
	)
	address = forms.CharField(
		required=True,
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Address'
			}
		)
	)
	
######################################################################
####CREATE SINGLE EVENT
@view_function
@permission_required('homepage.is_manager',login_url='/homepage/login/')
def create(request):
	
	event = hmod.Event()
	event.name = 'name'
	event.description = ''
	event.start_date = '1111-1-1'
	event.end_date = '1111-1-1'
	event.map_file = ''
	event.venue_name = ''
	event.address_id = '1'
	event.save()
	
	return HttpResponseRedirect('/homepage/events.edit/{}/'.format(event.id))


######################################################################
####DELETE SINGLE EVENT
@view_function
@permission_required('homepage.is_manager',login_url='/homepage/login/')
def delete(request):
	
	try:
		event = hmod.Event.objects.get(id=request.urlparams[0])
	except hmod.DoesNotExist:
		return HttpResponseRedirect('/homepage/events/')

	event.delete()

	return HttpResponseRedirect('/homepage/events/')
