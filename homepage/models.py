from django.db import models
from polymorphic import PolymorphicModel
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser



#########################################
####user models
class User(AbstractUser):
    ## these are inherited from abstractUser
    ## password
    ## last_login
    ## username
    ## first_name
    ## last_name
    ## email
    ## is_staff
    ## is_active
    ## date_joined

    ## MY STUFF STARTS HERE
    address = models.TextField()
    city = models.TextField(max_length=255)
    state = models.TextField()
    zip = models.IntegerField()
    def __str__(self):
        return self.username


# class Person(PolymorphicModel):
# 	address1 = models.TextField()
# 	address2 = models.TextField()
# 	city = models.TextField(max_length=255)
# 	state = models.TextField()
# 	zip = models.IntegerField()
# 	country = models.TextField()
# 	is_organization = models.BooleanField(default='false')
# 	organization_type = models.TextField()
# 	security_question = models.TextField()
# 	security_answer = models.TextField()
# 	user = models.OneToOneField(User)

# class Meta:
# 	abstract = True


# class Agent(Person):
# 	appointment_date = models.DateField()
#
# class Participant(Person):
# 	biographical_sketch = models.TextField()
# 	contact_relationship = models.TextField()
# 	id_photo = models.IntegerField()

class Photograph(models.Model):
	date_taken = models.DateField()
	place_taken = models.TextField()
	image = models.FileField()
	#person = models.ForeignKey(Person)
		
class PhotographableThing(models.Model):
	photograph = models.ManyToManyField(Photograph)
	#person = models.ForeignKey(Person)


class Phone(models.Model):
	number = models.IntegerField()
	extension = models.IntegerField()
	type = models.IntegerField()
	#person = models.ForeignKey(Person)

class Item(models.Model):
	name = models.TextField()
	description = models.TextField()
	value = models.IntegerField()
	standard_rental_price = models.IntegerField()
	rentable = models.BooleanField(default='false')
	#owner = models.ForeignKey(Person)

class Rental(models.Model):
	# agent = models
	rental_time = models.DateField()
	due_date = models.DateField()
	discount_percent = models.IntegerField()
	rentals = models.ManyToManyField(Item, through='RentedItem')

class RentedItem(models.Model):
	rental = models.ForeignKey(Rental)
	item = models.ForeignKey(Item)
	condition = models.TextField()
	new_damage = models.TextField()
	damage_fee = models.IntegerField()
	late_fee = models.IntegerField()

class WardrobeItem(Item):
	size = models.DecimalField(max_digits=5, decimal_places=2)
	size_modifier = models.DecimalField(max_digits=5, decimal_places=2)
	gender = models.BooleanField(default='false')
	color = models.TextField()
	pattern = models.TextField()
	start_year = models.DateField()
	end_year = models.DateField()
	note = models.TextField()

class Return(models.Model):
	return_time = models.DateField()
	fees_paid = models.DecimalField(max_digits=5, decimal_places=2)
	# agent = models.ForeignKey(Agent)

class Order(models.Model):
	order_date = models.DateField()
	date_packed = models.DateField()
	date_paid = models.DateField()
	date_shipped = models.DateField()
	tracking_number = models.IntegerField()
	#agent_packed_by = models.ForeignKey(Agent)
	#agent_payment_processed_by = models.ForeignKey(Agent)
	#agent_shipped_by = models.ForeignKey(Agent)

class Area(models.Model):
	area_name = models.TextField()
	description = models.TextField()
	place_number = models.TextField()

class Role(models.Model):
	area = models.ForeignKey(Area)
	# participant = models.ForeignKey(Participant)
	name = models.TextField()
	type = models.TextField()

class HistoricalRole(models.Model):
	name = models.TextField()
	birth_date = models.DateField()
	birth_place = models.DateField()
	death_date = models.DateField()
	death_place = models.TextField()
	biographical_note = models.TextField()
	is_fictional = models.BooleanField(default='false')

class ArtisanItem(models.Model):
	artisan_item_name = models.TextField()
	description = models.TextField()
	low_price = models.DecimalField(max_digits=5, decimal_places=2)
	high_price = models.DecimalField(max_digits=5, decimal_places=2)

class Product(PolymorphicModel):
	name = models.TextField()
	description = models.TextField()
	category = models.TextField()
	current_price = models.DecimalField(max_digits=5, decimal_places=2)

class BulkProduct(Product):
	quantity_on_hand = models.IntegerField()

class IndividualProduct(Product):
	date_made = models.DateField()

class CustomProduct(Product):
	order_form_name = models.TextField()
	production_time = models.DateField()

class Event(models.Model):
	name = models.TextField()
	start_date = models.DateField()
	end_date = models.DateField()
	map_file = models.FileField()

class Venue(models.Model):
	venue_name = models.TextField()
	address = models.TextField()
	city = models.TextField()
	state = models.TextField()
	zip = models.IntegerField()

class PublicEvent(models.Model):
	name = models.TextField()
	description = models.TextField()

class ProductPicture(models.Model):
	picture_file = models.FileField()
	caption = models.TextField()

class PublicEvent(models.Model):
	name = models.TextField()
	description = models.TextField()

class PersonalDetail(models.Model):
	order_file = models.TextField()

class BulkDetail(models.Model):
	quantity = models.IntegerField()
	price = models.DecimalField(max_digits=5, decimal_places=2)




