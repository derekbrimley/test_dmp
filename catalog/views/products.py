from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
import homepage.models as hmod
from django import forms
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import requests

templater = get_renderer('catalog')

########################################
##MAIN PRODUCT PAGE
@view_function
def process_request(request):
	template_vars = {}
	
	products = hmod.StockedProduct.objects.all()
	#print(items)
	
	# for product in products:
		# print('ID: ', product.id,' Quantity: ', product.quantity_on_hand,' Location: ',product.shelf_location)
		# for product_info in products_info:
			# if product_info.id == product.product_specification_id:
				# print('Product Info ID: ',product_info.id)
	
	template_vars['products'] = products

	# if 'shopping_cart' not in request.session:
		# request.session['shopping_cart'] = {}
	
	# if item.id not in request.session['shopping_cart']:
		# request.session['shopping_cart'][item.id] = 1
	# else:
		# request.session['shopping_cart'][item.id] += 1
	# print('>>>>>>>>>>>>>',request.session['hey'])
	
	return templater.render_to_response(request, 'products.html',template_vars)
	
######################################################################
#SHOWS LIST OF RENTABLEPRODUCTS
@view_function
def rentals(request):
	params = {}
	
	rentable_products = hmod.RentableProduct.objects.all()
	
	params['rentable_products'] = rentable_products
	
	return templater.render_to_response(request,'products.rentals.html',params)
		
	
########################################
##PRODUCT SEARCH
@view_function
def search(request):
	template_vars = {}
	
	form = ProductSearchForm()
	
	products = hmod.StockedProduct.objects.all()

	if request.method=="POST":
		form = ProductSearchForm(request.POST)
		search_term = request.POST['search_term']
		
		print(">>>>>>>>>>>>>>post")
		if form.is_valid():
			#COMPARE TEXT FROM USER TO DATABASE
			print(">>>>>>>>>>>>>>valid form")
			
			for product in products:
				print("search term: ",search_term," product: ",product.name)
				if search_term == product.name:
					print(product)
					template_vars['product'] = search_term
					return templater.render_to_response(request,'products.search.html',template_vars)
					
			template_vars['product'] = search_term
		
		else:
			print(">>>>>>>>>>>>>>form not valid")
			
	template_vars['form'] = form
	template_vars['products'] = products
	return templater.render_to_response(request, 'products.search.html',template_vars)

########################################
##PRODUCT DETAIL MODAL
@view_function
def detail_modal(request):
	template_vars = {}
	
	product = hmod.StockedProduct.objects.get(id=request.urlparams[0])
	
	template_vars['product'] = product
	
	return templater.render_to_response(request,'products.detail_modal.html',template_vars)
	
	
########################################
##PRODUCT DETAIL
@view_function
def detail(request):
	template_vars = {}
	
	product = hmod.StockedProduct.objects.get(id=request.urlparams[0])
	# print('>>>>>>>>>>>>>>>>',product.product_specification.id)
	
	template_vars['product'] = product
	
	return templater.render_to_response(request,'products.detail.html',template_vars)

########################################
##RENTAL DETAIL
@view_function
def rental_detail(request):
	template_vars = {}
	
	rentable_product = hmod.RentableProduct.objects.get(id=request.urlparams[0])
	# print('>>>>>>>>>>>>>>>>',product.product_specification.id)
	
	template_vars['rentable_product'] = rentable_product
	
	return templater.render_to_response(request,'products.rental_detail.html',template_vars)
	
########################################
##SHOPPING CART	
@view_function
def shopping_cart(request):
	template_vars = {}	
	
	product_id = request.urlparams[0]
	shopping_cart = request.session.get('shopping_cart', {})

	total_price = 0
	
	print('>>>>>>>>>>>',shopping_cart)
	items = []
	
	for product_id in shopping_cart:
		
		product = hmod.StockedProduct.objects.get(id=product_id)
		quantity = shopping_cart.get(product_id)
		price = int(product.price) * int(quantity)
		total_price += price
		items.append(product)
		print(product.id)

	
	template_vars['shopping_cart'] = shopping_cart
	template_vars['items'] = items
	template_vars['total_price'] = total_price
	
	return templater.render_to_response(request,'products.shopping_cart.html',template_vars)
	
	
########################################
##RENTAL CART	
@view_function
def rental_cart(request):
	template_vars = {}	
	
	product_id = request.urlparams[0]
	rental_cart = request.session.get('rental_cart', {})

	total_price = 0
	
	print('>>>>>>>>>>>',rental_cart)
	items = []
	
	for product_id in rental_cart:
		
		product = hmod.StockedProduct.objects.get(id=product_id)
		quantity = rental_cart.get(product_id)
		price = int(product.price) * int(quantity)
		total_price += price
		items.append(product)
		print(product.id)

	
	template_vars['rental_cart'] = rental_cart
	template_vars['items'] = items
	template_vars['total_price'] = total_price
	
	return templater.render_to_response(request,'products.rental_cart.html',template_vars)

	
########################################
##ADD PRODUCT TO SHOPPING CART	
@view_function
def add_item(request):
	template_vars = {}	
	
	product_id = request.urlparams[0]
	quantity = request.urlparams[1]
	
	product = hmod.StockedProduct.objects.get(id=product_id)
	
	shopping_cart = 	request.session.get('shopping_cart',{})
	
	print('>>>>>>>>>>>>>',product.id)
	try:
		if 'shopping_cart' not in request.session:
			request.session['shopping_cart'] = {}
	except:
		return HttpResponseRedirect('/account/products')
		
	if product_id in request.session['shopping_cart']:
		current_quantity = request.session['shopping_cart'][product_id]
		new_quantity = int(current_quantity) + int(quantity)
		request.session['shopping_cart'][product_id] = new_quantity
	else:
		request.session['shopping_cart'][product_id] = quantity
	request.session.modified = True
		
	print("Your item id(which is the 'key' or 'position' in your dictionary): " + str(product_id))
	print("Its value(the quantity of the specific item in your cart): " + str(request.session['shopping_cart'][product_id]))

	return HttpResponseRedirect('/catalog/products.shopping_cart/')

########################################
##ADD PRODUCT TO RENTAL CART	
@view_function
def add_rental_item(request):
	template_vars = {}	
	
	product_id = request.urlparams[0]
	quantity = request.urlparams[1]
	
	product = hmod.RentableProduct.objects.get(id=product_id)
	
	rental_cart = 	request.session.get('rental_cart',{})
	
	print('>>>>>>>>>>>>>',product.id)
	try:
		if 'rental_cart' not in request.session:
			request.session['rental_cart'] = {}
	except:
		return HttpResponseRedirect('/account/products')
		
	if product_id in request.session['rental_cart']:
		current_quantity = request.session['rental_cart'][product_id]
		new_quantity = int(current_quantity) + int(quantity)
		request.session['rental_cart'][product_id] = new_quantity
	else:
		request.session['rental_cart'][product_id] = quantity
	request.session.modified = True
		
	print("Your item id(which is the 'key' or 'position' in your dictionary): " + str(product_id))
	print("Its value(the quantity of the specific item in your cart): " + str(request.session['rental_cart'][product_id]))

	return HttpResponseRedirect('/catalog/products.rental_cart/')

########################################
##DELETE PRODUCT	
@view_function
def delete(request):
	template_vars = {}
	
	shopping_cart = request.session.get('shopping_cart',{})
	product_id = request.urlparams[0]
	
	if product_id in shopping_cart:
		del shopping_cart[product_id]
		print(">>>>>>>>>>>>deleted")

	request.session['shopping_cart'] = shopping_cart
	request.session.modified = True
	
	return HttpResponseRedirect('/catalog/products.shopping_cart/')

########################################
##DELETE RENTAL PRODUCT	
@view_function
def delete_rental(request):
	template_vars = {}
	
	rental_cart = request.session.get('rental_cart',{})
	product_id = request.urlparams[0]
	
	if product_id in rental_cart:
		del rental_cart[product_id]
		print(">>>>>>>>>>>>deleted")
	
	request.session['rental_cart'] = rental_cart
	request.session.modified = True
	
	return HttpResponseRedirect('/catalog/products.rental_cart/')
	
########################################
##DELETE SHOPPING CART	
@view_function
def delete_cart(request):
	template_vars = {}
	
	try:
		if 'shopping_cart' in request.session:
			request.session['shopping_cart'] = {}
			del shopping_cart
			print(">>>>>>>>>>>CART DELETED")
			request.session.modified = True
		elif 'rental_cart' in request.session:
			request.session['rental_cart'] = {}
			del rental_cart
			request.session.modified = True

	except:
		return HttpResponseRedirect('/catalog/products')
	
########################################
##CHECKOUT
@view_function
@login_required(login_url='/account/login/')
def checkout(request):
	template_vars = {}
	
	product_id = request.urlparams[0]
	shopping_cart = request.session.get('shopping_cart', {})

	total_price = 0
	
	print('>>>>>>>>>>>',shopping_cart)
	items = []
	
	for product_id in shopping_cart:
		
		product = hmod.StockedProduct.objects.get(id=product_id)
		quantity = shopping_cart.get(product_id)
		price = int(product.price) * int(quantity)
		total_price += price
		items.append(product)
		print(product.id)
	
	template_vars['shopping_cart'] = shopping_cart
	template_vars['items'] = items
	template_vars['total_price'] = total_price
	
	return templater.render_to_response(request,'products.checkout.html',template_vars)

########################################
##CHECKOUT RENTAL
@view_function
def rental_checkout(request):
	template_vars = {}
	
	product_id = request.urlparams[0]
	rental_cart = request.session.get('rental_cart', {})

	total_price = 0
	
	print('>>>>>>>>>>>',rental_cart)
	items = []
	
	for product_id in rental_cart:
		
		product = hmod.RentableProduct.objects.get(id=product_id)
		quantity = rental_cart.get(product_id)
		price = int(product.price) * int(quantity)
		total_price += price
		items.append(product)
		print(product.id)
	
	template_vars['rental_cart'] = rental_cart
	template_vars['items'] = items
	template_vars['total_price'] = total_price
	
	return templater.render_to_response(request,'products.rental_checkout.html',template_vars)
	
########################################
##THANK YOU
@view_function
def thankyou(request):
	template_vars = {}
	
	API_KEY = '122ecd484ee55a9588c4fcbf343e8d5a'
	API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'	
	
	form = BillingForm()
	billing_info = []
	total_price = 0
	shopping_cart = request.session.get('shopping_cart', {})
	items = []
	
	user = hmod.User.objects.get(username=request.user.username)
	email = user.email
	
	
	for product_id in shopping_cart:
		product = hmod.StockedProduct.objects.get(id=product_id)
		quantity = shopping_cart.get(product_id)
		price = int(product.price) * int(quantity)
		total_price += price
		items.append(product)
		
	if request.method=="POST":
		form = BillingForm(request.POST)
		print("post")
		if form.is_valid():
			card_name = form.cleaned_data['card_name']
			address = form.cleaned_data['address']
			city = form.cleaned_data['city']
			zip = form.cleaned_data['zip']
			state = form.cleaned_data['state']
			card_type = form.cleaned_data['card_type']
			card_number = form.cleaned_data['card_number']
			expiration_month = form.cleaned_data['expiration_month']
			expiration_year = form.cleaned_data['expiration_year']
			cvc = form.cleaned_data['cvc']
			
			r = requests.post(API_URL, data={
				'apiKey': API_KEY,
				'currency': 'usd',
				'amount': total_price,
				'type': card_type,
				'number': card_number,
				'exp_month': expiration_month,
				'exp_year': expiration_year,
				'cvc': cvc,
				'name': card_name,
				'description': "Charge for {} {}".format(user.first_name,user.last_name),
			})
			
			# print(r.text)
			
			resp = r.json()
			if 'error' in resp:
				print("ERROR: ", resp['error'])
			else:
				print(resp.keys())
				print(resp['ID'])
				
				charge_id = resp['ID']
				
				billing_info = [address,city,zip,state,card_type,card_number,expiration_month,expiration_year,cvc];
				
				template_vars['billing_info'] = billing_info
				
				send_mail('Purchase Confirmation {}'.format(charge_id), 'Your card has been successfully charged ${} for your purchases. Thank you! If you have any questions about your purchase, please call 801-422-8080'.format(total_price), 'derekbrimley@gmail.com',[email], fail_silently=False)
				shopping_cart = 	request.session.get('shopping_cart',{})
				
				transaction = hmod.Transaction()
				transaction.date = datetime.now()
				transaction.date_packed = datetime.now()
				transaction.date_paid = datetime.now()
				transaction.payment_handler_id = 10
				transaction.date_shipped = datetime.now()
				transaction.tracking_number = 12345
				transaction.shipped_by_id = 10
				transaction.ships_to = user.address
				transaction.packed_by_id = 10
				transaction.payment_processed_by_id = 10
				transaction.shipped_by_id = 10
				transaction.handled_by_id = 10
				transaction.customer_id = user.id
				
				for product_id in shopping_cart:
					sale_item = hmod.SaleItem()
					sale_item.quantity = shopping_cart.get(product_id)
					sale_item.item_id = product_id
					sale_item.price = product.price
					sale_item.transaction_id = transaction.id
					
					sale_item.save()
				
				transaction.save()
				
				template_vars['shopping_cart'] = shopping_cart
				template_vars['items'] = items
				template_vars['total_price'] = total_price
				template_vars['form'] = form
				template_vars['billing_info'] = billing_info	
				
				return templater.render_to_response(request,'products.thankyou.html',template_vars)
	
	template_vars['shopping_cart'] = shopping_cart
	template_vars['items'] = items
	template_vars['total_price'] = total_price
	template_vars['form'] = form
	template_vars['billing_info'] = billing_info
	
	return templater.render_to_response(request,'products.billing.html',template_vars)
	
class BillingForm(forms.Form):
	card_name = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Name on card'
			}
		)
	)
	address = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Address'
			}
		)
	)
	city = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'City'
			}
		)
	)
	state = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'City'
			}
		)
	)
	zip = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Zip'
			}
		)
	)
	card_type = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Card Type'
			}
		)
	)
	card_number = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Card Number'
			}
		)
	)
	expiration_month = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Expiration Month'
			}
		)
	)
	expiration_year = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Expiration Year'
			}
		)
	)
	cvc = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'CVC Number'
			}
		)
	)

class ProductSearchForm(forms.Form):
	search_term = forms.CharField(
		widget=forms.TextInput(
			attrs={
			}
		)
	)