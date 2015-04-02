from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime, date, timedelta
import homepage.models as hmod
from django import forms
from django.contrib.auth.decorators import login_required


templater = get_renderer('homepage')

########################################
#MAIN BATCH PROCESS
@view_function
def process_request(request):
	template_vars = {}
	
	
	return templater.render_to_response(request, 'batch_processes.html',template_vars)
	
########################################
##OVERDUE RENTALS
@view_function
def overdue_rentals(request):
	template_vars = {}
	
	today_date = datetime.now().date()
	
	rental_items = hmod.RentalItem.objects.all()
	rentable_products = hmod.RentableProduct.objects.all()
	transactions = hmod.Transaction.objects.all()
	users = hmod.User.objects.all()
	
	overdue_rentals = []
	overdue_items = []
	
	for rental_item in rental_items:
		item_due_date = rental_item.date_due
		if today_date > item_due_date:
			overdue_rental = hmod.RentalItem.objects.get(id=rental_item.id)
			overdue_rentals.append(overdue_rental)
			
	print ("OVERDUE RENTALS: ",overdue_rentals)
	print ("rentable_products: ",rentable_products)
	template_vars['overdue_rentals'] = overdue_rentals
	template_vars['rentable_products'] = rentable_products
	
	return templater.render_to_response(request, 'overdue_rentals.html',template_vars)
	
########################################
##OVER 30
@view_function
def over_30(request):
	template_vars = {}
	
	today_date = datetime.now().date()
	
	rental_items = hmod.RentalItem.objects.all()
	rentable_products = hmod.RentableProduct.objects.all()
	transactions = hmod.Transaction.objects.all()
	users = hmod.User.objects.all()
	
	overdue_rentals = []
	overdue_items = []
	
	for rental_item in rental_items:
		item_due_date = rental_item.date_due
		if today_date - timedelta(days=30) >= item_due_date and today_date - timedelta(days=60) < item_due_date:
			overdue_rental = hmod.RentalItem.objects.get(id=rental_item.id)
			overdue_rentals.append(overdue_rental)
			
	print ("OVERDUE RENTALS: ",overdue_rentals)
	print ("rentable_products: ",rentable_products)
	template_vars['overdue_rentals'] = overdue_rentals
	template_vars['rentable_products'] = rentable_products
	
	return templater.render_to_response(request, 'over_30.html',template_vars)


########################################
##OVER 60
@view_function
def over_60(request):
	template_vars = {}
	
	today_date = datetime.now().date()
	
	rental_items = hmod.RentalItem.objects.all()
	rentable_products = hmod.RentableProduct.objects.all()
	transactions = hmod.Transaction.objects.all()
	users = hmod.User.objects.all()
	
	overdue_rentals = []
	overdue_items = []
	
	for rental_item in rental_items:
		item_due_date = rental_item.date_due
		if today_date - timedelta(days=60) >= item_due_date and today_date - timedelta(days=90) < item_due_date:
			overdue_rental = hmod.RentalItem.objects.get(id=rental_item.id)
			overdue_rentals.append(overdue_rental)
			
	print ("OVERDUE RENTALS: ",overdue_rentals)
	print ("rentable_products: ",rentable_products)
	template_vars['overdue_rentals'] = overdue_rentals
	template_vars['rentable_products'] = rentable_products
	
	return templater.render_to_response(request, 'over_60.html',template_vars)

########################################
##OVER 90
@view_function
def over_90(request):
	template_vars = {}
	
	today_date = datetime.now().date()
	
	rental_items = hmod.RentalItem.objects.all()
	rentable_products = hmod.RentableProduct.objects.all()
	transactions = hmod.Transaction.objects.all()
	users = hmod.User.objects.all()
	
	overdue_rentals = []
	
	for rental_item in rental_items:
		item_due_date = rental_item.date_due
		if today_date - timedelta(days=90) >= item_due_date:
			overdue_rental = hmod.RentalItem.objects.get(id=rental_item.id)
			overdue_rentals.append(overdue_rental)
			
	print ("OVERDUE RENTALS: ",overdue_rentals)
	print ("rentable_products: ",rentable_products)
	template_vars['overdue_rentals'] = overdue_rentals
	template_vars['rentable_products'] = rentable_products
	
	return templater.render_to_response(request, 'over_90.html',template_vars)
	
########################################
##EMAIL USERS
@view_function
def email_users(request):	
	template_vars = {}
	
	users = []
	emails = []
	
	today_date = datetime.now().date()
	
	rental_items = hmod.RentalItem.objects.all()
	transactions = hmod.Transaction.objects.all()
	
	overdue_rentals = []
	
	for rental_item in rental_items:
		item_due_date = rental_item.date_due
		if today_date - timedelta(days=90) >= item_due_date:
			overdue_rental = hmod.RentalItem.objects.get(id=rental_item.id)
			overdue_rentals.append(overdue_rental)
	
	for overdue_rental in overdue_rentals:
		transaction_id = overdue_rental.transaction_id
		transaction = hmod.Transaction.objects.get(id=transaction_id)
		user_id = transaction.customer_id
		user = hmod.User.objects.get(id=user_id)
		email = user.email
		if email not in emails:
			emails.append(email)
			
	for email in emails:
		
		
	print('EMAILS: ',emails)
	template_vars['emails'] = emails
	return templater.render_to_response(request, 'emails_sent.html',template_vars)

