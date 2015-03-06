from django.conf import settings
from django.http import HttpResponse
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
import homepage.models as hmod
from django import forms


templater = get_renderer('catalog')

########################################
##MAIN PRODUCT PAGE
@view_function
def process_request(request):
	template_vars = {}
	
	products = hmod.StockedProduct.objects.all()
	products_info = hmod.ProductSpecification.objects.all()
	#print(items)
	
	# for product in products:
		# print('ID: ', product.id,' Quantity: ', product.quantity_on_hand,' Location: ',product.shelf_location)
		# for product_info in products_info:
			# if product_info.id == product.product_specification_id:
				# print('Product Info ID: ',product_info.id)
	
	template_vars['products'] = products
	template_vars['products_info'] = products_info

	# if 'shopping_cart' not in request.session:
		# request.session['shopping_cart'] = {}
	
	# if item.id not in request.session['shopping_cart']:
		# request.session['shopping_cart'][item.id] = 1
	# else:
		# request.session['shopping_cart'][item.id] += 1
	# print('>>>>>>>>>>>>>',request.session['hey'])
	
	return templater.render_to_response(request, 'products.html',template_vars)
	
########################################
##PRODUCT SEARCH
@view_function
def search(request):
	template_vars = {}
	
	form = ProductSearchForm()
	
	products = hmod.ProductSpecification.objects.all()

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
					template_vars['products'] = products
					
			return templater.render_to_response(request,'search.results.html',template_vars)
		
		else:
			print(">>>>>>>>>>>>>>form not valid")
			
	template_vars['form'] = form
	template_vars['products'] = products
	return templater.render_to_response(request, 'products.search.html',template_vars)

class ProductSearchForm(forms.Form):
	search_term = forms.CharField(
		widget=forms.TextInput(
			attrs={
			}
		)
	)