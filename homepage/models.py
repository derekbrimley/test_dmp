##
## Name: 			Derek Brimley
## Author: 			Group 1-13
## Last Modified:	3/4/2015
##
## Description:		Models file for the CHF Case
##
##
##

from django.db import models
from polymorphic import PolymorphicModel
from django.contrib.auth.models import AbstractUser

class Address(models.Model):
	##MAILING ADDRESS
	address1 = models.TextField(max_length=200)
	address2 = models.TextField(max_length=200, null=True, blank=True)
	city = models.TextField(max_length=100)
	state = models.TextField(max_length=20)
	zip = models.TextField(max_length=20)
	
	# class Meta:
	# 	ordering = ['state', 'city', 'zip', 'address1', 'address2']
	# 	verbose_name_plural = 'addresses'
		
	# def __str__(self):
	# 	return '{} {} {}, {} {}'.format(self.street1, self.street2, self.city, self.state, self.zip_code)

	
class User(AbstractUser):
    ## ATTRIBUTES INHERITED FROM ABSTRACT USERS
    ## password
    ## last_login
    ## username
    ## first_name
    ## last_name
    ## email
    ## is_staff
    ## is_active
    ## date_joined

    ## EXTENDED ATTRIBUTES
	organization_name = models.TextField(max_length=200, null=True, blank=True)
	organization_type = models.TextField(max_length=40, null=True, blank=True)
	security_question = models.TextField(max_length=200)
	security_answer = models.TextField(max_length=200)
	phone = models.TextField(max_length=40)
	requires_reset = models.BooleanField(default=False)
	date_appointed_agent = models.DateField(null=True)
	bio_sketch = models.TextField(max_length=200, null=True, blank=True)
	relationship = models.TextField(max_length=200, null=True, blank=True)
	emergency_contact = models.TextField(max_length=200, null=True, blank=True)
	emergency_phone = models.TextField(max_length=200, null=True, blank=True)
	emergency_relationship = models.TextField(max_length=200, null=True, blank=True)
	address = models.ForeignKey(Address, related_name='+')
	# def __str__(self):
	# 	return self.user.username

class Photograph(models.Model):
	##PHOTOGRAPH OF ITEMS OR PEOPLE
    date_taken = models.DateField(max_length=200, null=True, blank=True)
    place_taken = models.TextField(max_length=1000, null=True, blank=True)
    user = models.ForeignKey(User, related_name='+',null=True) #Change username to user
    image = models.TextField(null=True, blank=True) #Change from Binaryfield to texF

class HistoricalFigure(models.Model):
	##HISTORICAL FIGURE THAT WILL BE PORTRAYED AT EVENT
	name = models.TextField(max_length=200)
	birth_date = models.DateField(null=True)
	birth_place = models.TextField(max_length=200, null=True, blank=True)
	death_date = models.DateField(null=True)
	death_place = models.TextField(max_length=200, null=True, blank=True)
	biographical_note = models.TextField()
	is_fictional = models.BooleanField(default=False)

class Event(models.Model):
	##INSTANCE OF EVENT
	name = models.TextField(max_length=200)
	description = models.TextField(max_length=1000)
	start_date = models.DateField()
	end_date = models.DateField()
	map_file = models.TextField(max_length=200) # changed from filefield to textfield
	venue_name = models.TextField(max_length=200)
	address = models.ForeignKey(Address, related_name='+') # changed from address
	
class Area(models.Model):
	##LOCATION WITHIN EVENT
	area_name = models.TextField(max_length=200)
	description = models.TextField(max_length=1000)
	place_number = models.PositiveIntegerField()
	coordinator = models.ForeignKey(User, related_name='coordinates')
	supervisor = models.ForeignKey(User, related_name='supervises')
	event = models.ForeignKey(Event)
	participants = models.ManyToManyField('User')
	
class UserRole(models.Model):
	##ASSOCIATION CLASS BETWEEN USER AND AREA. REPRESENTS A USER THAT IS ASSIGNED
	##TO PLAY A HISTORICAL ROLE AT A SPECIFIC AREA
	area = models.ForeignKey(Area)
	participant = models.ForeignKey(User)
	name = models.TextField(max_length=200)
	type = models.TextField(max_length=40)
	historical_figure = models.ForeignKey(HistoricalFigure, related_name='+', null=True )
	
class ExpectedSaleItem(models.Model):
	##ITEM THAT WILL BE SOLD AT A SPECIFIC AREA AT EVENT
	name = models.TextField(max_length=200)
	description = models.TextField(max_length=1000)
	low_price = models.DecimalField(max_digits=10, decimal_places=2)
	high_price = models.DecimalField(max_digits=10, decimal_places=2)
	photo = models.ForeignKey(Photograph, related_name='+', null=True)

class Transaction(models.Model):
	##SINGLE TRANSACTION: ORDER, RENTAL, RETURN, FEE
	date = models.DateField()
	date_packed = models.DateField()
	packed_by = models.ForeignKey(User)
	date_paid = models.DateField(null=True)
	payment_handler = models.ForeignKey(User)
	date_shipped = models.DateField(null=True)
	shipped_by = models.ForeignKey(User)
	tracking_number = models.TextField(null=True)
	ships_to = models.ForeignKey('Address', related_name='+')
	packed_by = models.ForeignKey('User', related_name='packedby_set')
	payment_processed_by = models.ForeignKey('User', related_name='paymentprocessedby_set')
	shipped_by = models.ForeignKey('User', related_name='shippedby_set')
	handled_by = models.ForeignKey('User', related_name='handledby_set')
	customer = models.ForeignKey('User', related_name='orders')
	



class Category(models.Model):
	##CLASS TO CATEGORIZE PRODUCTS
	description = models.TextField(max_length=200)
	
	class Meta:
		verbose_name_plural = 'categories'
	
	def __str__(self):
		return self.description
	
class ProductSpecification(models.Model):
	##DETAILS ABOUT A PRODUCT
	name = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	description = models.TextField()
	manufacturer = models.TextField()
	average_cost = models.DecimalField(max_digits=10, decimal_places=2)
	sku = models.TextField()
	order_form_name = models.TextField()
	production_time = models.DateField()
	
	# def __str__(self):
		# return '{} {}'.format(self.name, self.price)

################################################################################ HOW?
class StockedProduct(PolymorphicModel): #changed to polymorphic model
	##PRODUCTS THAT ORGANIZATION IS CURRENTLY TRACKING
	quantity_on_hand = models.IntegerField(null=True)
	shelf_location = models.TextField(null=True)
	order_file = models.TextField(null=True)
	product_specification = models.ForeignKey('ProductSpecification')

	# def __str__(self):
		# return '{}'.format(self.quantity_on_hand)

class SerializedProduct(StockedProduct):
	#Serialized Product
	serial_number = models.TextField(null=False)
	date_acquired = models.TextField(null=True)
	cost = models.DecimalField(max_digits=10, decimal_places=2,null=True)
	status = models.TextField(null=True)
	for_sale = models.BooleanField(default=False)
	condition_new = models.BooleanField(default=False)
	is_rentable = models.BooleanField(default=False)
	notes = models.TextField(null=True)
	
	# def __str__(self):
		# return '{} {}'.format(self.serial_number, self.status)
	
class WardrobeItem(SerializedProduct):
	##WARDROBE ITEM IN INVENTORY
	size = models.TextField(null=True)
	size_modifier = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	gender = models.TextField(max_length=40, null=True)
	color = models.TextField(max_length=40, null=True)
	pattern = models.TextField(max_length=40, null=True)
	start_year = models.PositiveIntegerField(null=True)
	end_year = models.PositiveIntegerField(null=True)
	note = models.TextField(null=True)
	
class RentableProduct(SerializedProduct):
	##ITEM IN INVENTORY THAT CAN BE RENTED
	times_rented = models.IntegerField()
	price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
	replacement_price = models.DecimalField(max_digits=10, decimal_places=2)
	
	# def __str__(self):
		# return '{} {} {}'.format(self.times_rented, self.price_per_day, self.replacement_price)

class LineItem(PolymorphicModel):
	##LINE ITEM IN A TRANSACTION
	price = models.DecimalField(max_digits=10, decimal_places=2)
	transaction = models.ForeignKey(Transaction)
	
	class Meta:
		abstract = True
		
class SaleItem(LineItem):
	##TYPE OF TRANSACTION FOR SALES
	quantity = models.IntegerField()
	item = models.ForeignKey(StockedProduct, related_name='+')

	def __str__(self):
		return '{} {}'.format(self.amount, self.quantity)

class RentalItem(LineItem):
	##TYPE OF TRANSACTION LINE ITEM
	date_out = models.DateField(null=False)
	date_in = models.DateField(null=True)
	date_due = models.DateField(null=True)
	discount_percent = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	rentable_product = models.ForeignKey(StockedProduct, null=True)
	
	
	def __str__(self):
		return '{} {} {}'.format(self.date_out, self.date_due, self.date_in)
	
class Fee(LineItem):
	##TYPE OF TRANSACTION WHEN FEES ASSIGNED--ABSTRACT
	waived = models.BooleanField(default=True)
	rental_item = models.ForeignKey(RentalItem, related_name='+')
	
	class Meta:
		abstract = True

class LateFee(Fee):
	##CONCRETE SUBCLASS OF FEE FOR LATE RETURNS
	days_late = models.IntegerField()
	
	def __str__(self):
		return '{} {} {}'.format(self.amount, self.days_late, self.waived)

class DamageFee(Fee):	
	##CONCRETE SUBCLASS OF FEE FOR DAMAGED RETURNS
	description = models.TextField()
	
	def __str__(self):
		return '{} {} {}'.format(self.amount, self.description, self.waived)
