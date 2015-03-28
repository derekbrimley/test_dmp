from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
import homepage.models as hmod
from django import forms
from django.contrib.auth.decorators import login_required


templater = get_renderer('homepage')

########################################
#MAIN BATCH PROCESS
@view_function
def process_request(request):
	template_vars = {}
	
	rental_items = hmod.RentalItem.objects.all()
	rentable_products = hmod.RentableProduct.objects.all()
	today_date = datetime.now().date()
	overdue_items = []
	overdue_items_info = []
	
	for rental_item in rental_items:
		item_due_date = rental_item.date_due
		if today_date > item_due_date:
			overdue_item_object = hmod.RentalItem.objects.get(id=rental_item.id)
			overdue_items.append(overdue_item_object)
			overdue_item_info = hmod.RentableProduct.objects.get(id=rental_item.rentable_product_id)
			overdue_items_info.append(overdue_item_info)
			
	print (overdue_items)
	template_vars['overdue_items'] = overdue_items
	template_vars['overdue_items_info'] = overdue_items_info
	
	return templater.render_to_response(request, 'batch_processes.html',template_vars)