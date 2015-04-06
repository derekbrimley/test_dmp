from django.conf import settings
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
import homepage.models as hmod

templater = get_renderer('homepage')

######################################################################
###RETURN LIST OF EVENTS
@view_function
def process_request(request):
	
	params = {}
	events = hmod.Event.objects.all()
	areas = hmod.Area.objects.all()

	params['areas'] = areas
	params['events'] = events
	
	return templater.render_to_response(request,'info.html',params)
	
######################################################################
###INFO FOR SINGLE EVENT
@view_function
def event_info(request):

	params = {}
	
	event_id = request.urlparams[0]
	event = hmod.Event.objects.get(id=event_id)
	areas = hmod.Area.objects.filter(event_id=event_id)
	sale_items = hmod.ExpectedSaleItem.objects.all()
	
	params['sale_items'] = sale_items 
	params['event'] = event
	params['areas'] = areas
	
	return templater.render_to_response(request,'info.event_info.html',params)