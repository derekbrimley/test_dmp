#!/usr/bin/env python

#initialize django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_dmp.settings'
import django
django.setup()


#regular imports
import homepage.models as hmod
import psycopg2
import sys

from django.db import connection
from django.contrib.auth.models import Group, Permission, ContentType
import subprocess


cursor = connection.cursor()
cursor.execute("DROP SCHEMA PUBLIC CASCADE")
cursor.execute("CREATE SCHEMA PUBLIC")
subprocess.call([sys.executable, "manage.py", "migrate"])
cursor.close()


#Address
for data in [	
	[ "100 Default", "Default", "AK", "99654" ],
	[ "25 E 900 N", "Provo", "Utah", "84604" ],
	[ "1250 E 800 N", "Provo", "Utah", "84604" ],
	[ "700 N 789 E", "Provo", "Utah", "84604" ],
	[ "880 S 4673 W", "Provo", "Utah", "84604" ],
	[ "880 S 4673 W", "Provo", "Utah", "84604" ],
	[ "25 E 900 N", "Provo", "Utah", "84604" ],
	[ "456 Victory", "Langley", "Virginia", "34652" ],
	[ "575 OneLife", "New York", "New York", "42566" ],
	[ "1 Greif ", "Malmedy", "Germany", "55624" ],
	[ "132 North Africa", "Calais", "Virginia", "77485" ],
	[ "584 Bulge St", "West Point", "Virginia", "84733" ],
	[ "89 N 89 S", "Providence", "Rhode Island", "68556" ],
]:
	a = hmod.Address()
	a.address1 = data[0]
	a.city = data[1]
	a.state =data[2]
	a.zip = data[3]
	a.save()	


#User
for data in [
	[ "AdminFirst", "AdminLast", "adminP", "admin1", False, 1, "admin@chf.com", '801-423-1428', "What is your quest? [to seek the holy grail]", "to seek the holy grail" ],
	[ "ManagerFirst", "ManagerLast", "managerP", "manager1", False, 1, "manager@chf.com", '801-423-1428', "What is your quest? [to seek the holy grail]", "to seek the holy grail" ],
	[ "AgentFirst", "AgentLast", "agentP", "agent1", False, 1, "agent@chf.com",'801-423-1428', "What is your quest? [to seek the holy grail]", "to seek the holy grail"],
    [ "BakerFirst", "BakerLast", "bakerP", "baker1", False, 1, "baker@chf.com",'801-423-1428', "What is your quest? [to seek the holy grail]", "to seek the holy grail"],
    [ "CooperFirst", "CooperLast", "cooperP", "cooper1", False, 1, "cooper@chf.com", '801-423-1428', "What is your quest? [to seek the holy grail]", "to seek the holy grail"],
    [ "Customer1First", "Customer1Last", "customerP", "customer1", False, 1, "default@chf.com", '801-423-1428', "What is your quest? [to seek the holy grail]", "to seek the holy grail"],
    [ "Customer2First", "Customer2Last", "customerP", "customer2", False, 1, "default@chf.com", '801-423-1428', "What is your quest? [to seek the holy grail]", "to seek the holy grail"],
	[ "Dustin", "Belliston", "dustinP", "dustin1", False, 2, "default@chf.com", '801-423-1428', "What is your quest? [to seek the holy grail]", "to seek the holy grail"],
	[ "Izzy", "Beh", "izzyP", "izzy1", False, 2, "default@chf.com", '801-423-1428', "What is your quest? [to seek the holy grail]", "to seek the holy grail"],
	[ "Derek", "Brimley", "password", "drizzle", True, 3, "derekbrimley@gmail.com", '801-423-1428', "What is your quest? [to seek the holy grail]", "to seek the holy grail"],
	[ "John", "Blackburn", "johnP", "john1", False, 4, "default@chf.com", '801-423-1428', "What is your quest? [to seek the holy grail]", "to seek the holy grail"],
	[ "Kelly", "Blackburn", "kellyP", "kelly1", False, 5, "default@chf.com", '801-423-1428', "What is your quest? [to seek the holy grail]", "to seek the holy grail"],
	[ "Kalli", "Belliston", "kalliP", "kalli1", False, 6, "default@chf.com", '801-423-1428', "What is your quest? [to seek the holy grail]", "to seek the holy grail"],
	[ "George", "Washington", "georgeP", "george1", False, 7, "default@chf.com", '801-423-1428', "What is your quest? [to seek the holy grail]", "to seek the holy grail"],
	[ "Nathan", "Hale", "nathanP", "nathan1", False, 8, "default@chf.com", '801-423-1428', "What is your quest? [to seek the holy grail]", "to seek the holy grail"],
	[ "Otto", "Scorzeny", "ottoP", "otto1", False, 9, "default@chf.com", '801-423-1428', "What is your quest? [to seek the holy grail]", "to seek the holy grail"],
	[ "Erwin", "Rommel", "erwinP", "erwin1", False, 10, "default@chf.com", '801-423-1428', "What is your quest? [to seek the holy grail]", "to seek the holy grail"],
	[ "George", "Patton", "georgeP", "georges1", False, 11, "default@chf.com", '801-423-1428', "What is your quest? [to seek the holy grail]", "to seek the holy grail"],
	[ "Omar", "Bradley", "omarP", "omar1", False, 12, "default@chf.com", '801-423-1428', "What is your quest? [to seek the holy grail]", "to seek the holy grail"],   
]:
    u = hmod.User()
    u.first_name = data[0]
    u.last_name = data[1]
    u.set_password(data[2])
    u.username = data[3]
    u.is_superuser = data[4]
    u.address_id = data[5]
    u.email = data[6]
    u.phone = data[7]
    u.security_question = data[8]
    u.security_answer = data[9]

    u.save()



#####Permissions#####
##Code from Carter Hesterman
# Permission.objects.all().delete()
# Group.objects.all().delete()
# permission = Permission()
# permission.codename = 'manager_rights'
# permission.content_type = ContentType.objects.get(id=7)
# permission.name = 'Has Manager Rights'
# permission.save()
# group = Group()
# group.name = "Managers"
# group.save()
# group.permissions.add(permission)
# print('permissions initialized')


con = None
try:    
    con = psycopg2.connect("dbname='derek_db' user='postgres' password='password'")   
    cur = con.cursor()    
    #cur.execute("CREATE TABLE Cars(Id INTEGER PRIMARY KEY, Name VARCHAR(20), Price INT)")

    #Create 3 groups
    cur.execute("INSERT INTO auth_group VALUES(1,'admin')")
    cur.execute("INSERT INTO auth_group VALUES(2,'manager')")
    cur.execute("INSERT INTO auth_group VALUES(3,'agent')")
    
    #Give the 3 groups the permissions
    cur.execute("INSERT INTO auth_group_permissions VALUES(1, 1, 1)")
    cur.execute("INSERT INTO auth_group_permissions VALUES(2, 1, 2)")
    cur.execute("INSERT INTO auth_group_permissions VALUES(3, 1, 3)")
    cur.execute("INSERT INTO auth_group_permissions VALUES(4, 2, 2)")
    cur.execute("INSERT INTO auth_group_permissions VALUES(5, 2, 3)")
    cur.execute("INSERT INTO auth_group_permissions VALUES(6, 3, 3)")

    #Update the permissions that where generated
    cur.execute("UPDATE auth_permission SET name='admin level', codename='is_admin' WHERE id='1'")
    cur.execute("UPDATE auth_permission SET name='manager level', codename='is_manager' WHERE id='2'")
    cur.execute("UPDATE auth_permission SET name='agent level', codename='is_agent' WHERE id='3'")
    
    #Update the first content type to be [homepage.%]
    cur.execute("UPDATE django_content_type SET name='derek_db', app_label='homepage', model='test_dmp' WHERE id='1'")

    #Put the first three users into the groups
    cur.execute("INSERT INTO homepage_user_groups VALUES(1, 1, 1)")
    cur.execute("INSERT INTO homepage_user_groups VALUES(2, 2, 2)")
    cur.execute("INSERT INTO homepage_user_groups VALUES(3, 3, 3)")

    con.commit()
    
except:
    print("error")  
    sys.exit(1)
       
finally: 
    if con:
        con.close()
#^^^^^Permissions^^^^^#

#Photograph
for data in [
    [ '2015-01-01', "Colonial Event", 1, "shop-placeholder.png"],
    [ '2015-01-01', "Colonial Event", 2, "shop-placeholder.png"],
]:
    u = hmod.Photograph()
    u.date_taken = data[0]
    u.place_taken = data[1]
    u.user_id = data[2]
    u.image = data[3]
    u.save()


#HistoricalFigure
for data in [
    [ "Benjamim Franklin", '1706-01-17', "Boston", '1790-04-17', "Philedelphia", 
        """He was one of the most extraordinary human beings the world has
        ever known. Born into the family of a Boston candle maker, Benjamin
        Franklin became the most famous American of his time. He helped
        found a new nation and defined the American character. Writer,
        inventor, diplomat, businessman, musician, scientist, humorist,
        civic leader, international celebrity . . . genius. 
        Explore the life of a remarkable man.""", False],
    [ "Alexander Hamilton", '1755-01-11', "Charleston", '1804-07-12', "New York", 
        """Hamilton became the leading cabinet member in the new government under President Washington.
        Hamilton was a nationalist, who emphasized strong central government and successfully argued 
        that the implied powers of the Constitution provided the legal authority to fund the national debt, 
        assume states' debts, and create the government-owned Bank of the United States.""", False],
    [ "John Cooper", '1714-05-05', "Coopertown", '1804-07-12', "Coopertown", 
        """Most famous cooper in town. Made the barrels used in the Boston Tea Party!""", True],
]:

    u = hmod.HistoricalFigure()
    u.name = data[0]
    u.birth_date = data[1]
    u.birth_place = data[2]
    u.death_date = data[3]
    u.death_place = data[4]
    u.biographical_note = data[5]
    is_fictional = data[6]
    u.save()


#Event
for data in [
	[ "Colonial Heritage July 4", "Annual Celebration on July 4th. Celebrate our Indepedence!", '2015-07-04', '2015-07-04', "file", "Scera Outdoor Ampitheater", 1 ],
	[ "Heritage Expo", "Come see the many wonders of the Colonial time period", '2015-10-10', '2015-10-10', "file2", "UVU Center", 2 ],
	[ "Battle of Bunker Hill Reenactment", "A realistic and historically accurate reenactment of one of the most famous battles of the Revolution", '2015-08-16', '2015-08-18', "file3", "Kiwanis Park", 3 ],
]:
    u = hmod.Event()
    u.name = data[0]
    u.description = data[1]
    u.start_date = data[2]
    u.end_date = data[3]
    u.map_file = data[4]
    u.venue_name = data[5]
    u.address_id = data[6]
    u.save()


#Area
for data in [
    [ "Bakery", "This is where the bread is baked.", 1, 1, 2, 1 ],
    [ "Blacksmith", "This is where the metal is pounded.", 2, 1, 2, 1 ],
    [ "Seamtress", "This is where the thread is sewn.", 3, 1, 2, 1 ],
    [ "Archery", "This is where the archers arch.", 4, 1, 2, 1 ],
    [ "Cooperage", "This is where the barrells are coopered.", 5, 1, 2, 1 ],
]:
    u = hmod.Area()
    u.area_name = data[0]
    u.description = data[1]
    u.place_number = data[2]
    u.coordinator_id = data[3]
    u.supervisor_id = data[4]
    u.event_id = data[5]
    #u.participants_id = data[6]
    u.save()


#UserRole
for data in [
    [ 5, 5, "Cooper", "Artisan", 3 ],
    [ 1, 4, "Baker", "Artisan",  None ],
]:
    u = hmod.UserRole()
    u.area_id = data[0]
    u.participant_id = data[1]
    u.name = data[2]
    u.type = data[3]
    u.historical_figure_id = data[4]
    u.save()


#ExpectedSaleItem
for data in [
    [ "Bread Pin", "A baker's rolling pin. An essential in the colonial kitchen!.", 10.00, 20.00, None,1 ],
    [ "Coopers Brush", "Used to give a nice stain to the new barrel.", 5.00, 20.00, None,5 ],
	[ "Butter Maker", "Used to make some butter.", 20.00, 80.00, None,1 ],
	[ "Horseshoe", "Souvenir horseshoe that patrons make themselves.", 5.00, 10.00, None,2 ],
	[ "Bonnet", "Old fashioned bonnet. For the ladies.", 10.00, 30.00, None,3 ],
]:
	u = hmod.ExpectedSaleItem()
	u.name = data[0] 
	u.description = data[1] 
	u.low_price =  data[2] 
	u.high_price = data[3] 
	u.photo = data[4] 
	u.area_id = data[5]
	u.save()


#Transaction
for data in [
    [ '2015-01-01', '2015-01-01', 3, '2015-01-01', 3, '2015-01-01', 3, "AA12345678", 1, 3, 3, 3, 3, 6],
    [ '2015-01-02', '2015-01-02', 3, '2015-01-02', 3, '2015-01-02', 3, "BB12345678", 1, 3, 3, 3, 3, 7],
    [ '2015-01-03', '2015-01-03', 3, '2015-01-03', 3, '2015-01-03', 3, "CC12345678", 1, 3, 3, 3, 3, 6],
    [ '2015-01-04', '2015-01-04', 3, '2015-01-04', 3, '2015-01-04', 3, "DD12345678", 1, 3, 3, 3, 3, 6],
    [ '2015-01-05', '2015-01-05', 3, '2015-01-05', 3, '2015-01-05', 3, "FF12345678", 1, 3, 3, 3, 3, 7],
    [ '2015-01-06', '2015-01-06', 3, '2015-01-06', 3, '2015-01-06', 3, "GG12345678", 1, 3, 3, 3, 3, 11],
    [ '2015-01-07', '2015-01-07', 3, '2015-01-07', 3, '2015-01-07', 3, "HH12345678", 1, 3, 3, 3, 3, 12],
    [ '2015-01-08', '2015-01-08', 3, '2015-01-08', 3, '2015-01-08', 3, "JJ12345678", 1, 3, 3, 3, 3, 13],
    [ '2015-01-09', '2015-01-09', 3, '2015-01-09', 3, '2015-01-09', 3, "KK12345678", 1, 3, 3, 3, 3, 14],
    [ '2015-01-10', '2015-01-10', 3, '2015-01-10', 3, '2015-01-10', 3, "LL12345678", 1, 3, 3, 3, 3, 15],
]:
    u = hmod.Transaction()
    u.date = data[0]
    u.date_packed = data[1]
    u.packed_by_id =data[2]
    u.date_paid =data[3]
    u.payment_handler_id = data[4]
    u.date_shipped = data[5]
    u.shipped_by_id =data[6]
    u.tracking_number =data[7]
    u.ships_to_id = data[8]
    u.packed_by_id =data[9] 
    u.payment_processed_by_id = data[10]
    u.shipped_by_id = data[11]
    u.handled_by_id = data[12]
    u.customer_id = data[13]
    u.save()

# StockedProduct
for data in [
    [ '50', "Top", "Order_File1", "Liberty Bell", 5.00, "A small replica of the liberty bell. A hot seller!", "Colonial Foundation", 5.00, "ABCDEF01", "Order for [Name Here]", "2014-06-06",1,"Collectible"],
    [ '50', "Bottom", "Order_File2", "Handkerchief", 3.00, "An old handkerchief. A hot seller!", "Colonial Heritage Foundation", 5.00, "ABCDEF02", "Order for [Name Here]", "2014-06-06",2,"Collectible"],
    [ '50', "Middle", "Order_File3", "Liberty Pen", 5.00, "A replica of an old pen. A hot seller!", "Colonial Heritage Foundation", 5.00, "ABCDEF03", "Order for [Name Here]", "2014-06-06",3,"Collectible"],
	
]:
	u = hmod.StockedProduct()
	u.quantity_on_hand = data[0]
	u.shelf_location = data[1]
	u.order_file = data[2]
	u.name = data[3]
	u.price = data[4]
	u.description = data[5]
	u.manufacturer = data[6]
	u.average_cost  = data[7]
	u.sku = data[8]
	u.order_form_name = data[9]
	u.production_time = data[10]
	u.vendor_id = data[11]
	u.category = data[12]
	u.save()

#SerializedProduct
for data in [
    [ '50', "Middle", "Order_File4", "Necklace", 15.00, "A necklace with an American flag pendant.", "Colonial Heritage Foundation", 15.00, "ABCDEF04", "Order form [Name Here]", "2014-06-06",4,"Clothing", "00001", '2014-01-01', 5.00, "Status", True, True, True, "Serialized Product 1: Necklace"],
    [ '50', "Middle", "Order_File5", "Liberty Bracelet", 15.00, "A Bracelet with an American flag pendant.", "Colonial Heritage Foundation", 15.00, "ABCDEF05", "Order form [Name Here]", "2014-06-06",5,"Clothing", "00002", '2014-01-01', 5.00, "Status", True, True, True, "Serialized Product 2: Bracelet"],
    [  '50', "Middle", "Order_File6", "Liberty Watch", 15.00, "A watch with an American flag pendant.", "Colonial Heritage Foundation", 15.00, "ABCDEF06", "Order form [Name Here]", "2014-06-06",6,"Clothing", "00003", '2014-01-01', 5.00, "Status", True, True, True, "Serialized Product 3: Watch"],
	
]:
	u = hmod.SerializedProduct()
	u.quantity_on_hand = data[0]
	u.shelf_location = data[1]
	u.order_file = data[2]

	u.name = data[3]
	u.price = data[4]
	u.description = data[5]
	u.manufacturer = data[6]
	u.average_cost  = data[7]
	u.sku = data[8]
	u.order_form_name = data[9]
	u.production_time = data[10]
	u.vendor_id = data[11]
	u.category = data[12]

	u.serial_number = [13]
	u.date_acquired = [14]
	u.cost = data[15]
	u.status = data[16]
	u.for_sale = data[17]
	u.condition_new = data[18]
	u.is_rentable = data[19]
	u.notes = data[20]
	u.save()

#WardrobeItem
for data in [
    [ '50', "Middle", "Order_File7", "Liberty Hat", 22.00, "A hat from the colonial time.", "Colonial Heritage Foundation", 15.00, "ABCDEF07", "Order for [Name Here]", "2014-06-06",7,"Clothing", "00007", '2014-01-01', 5.00, "Status", True, True, True, "Wardrobe Item 1: Hat", None, None, "Male", "Blue", None, 1770, 1870, "This is a hat"],
    [ '50', "Middle", "Order_File8", "Liberty Shirt", 22.00, "A shirt from the colonial time.", "Colonial Heritage Foundation", 15.00, "ABCDEF08", "Order for [Name Here]", "2014-06-06",8,"Clothing", "00008", '2014-01-01', 5.00, "Status", True, True, True, "Wardrobe Item 2: Shirt", 'M', None, "Male", "Blue", None, 1770, 1870, "This is a shirt"],
    [ '50', "Middle", "Order_File9", "Liberty Belt", 22.00, "A belt from the colonial time.", "Colonial Heritage Foundation", 15.00, "ABCDEF09", "Order for [Name Here]", "2014-06-06",9,"Clothing", "00009", '2014-01-01', 5.00, "Status", True, True, True, "Wardrobe Item 3: Belt", '30', None, "Male", "Blue", None, 1770, 1870, "This is a belt"],
    [ '50', "Middle", "Order_File10", "Liberty Pants", 22.00, "A pants from the colonial time.", "Colonial Heritage Foundation", 15.00, "ABCDEF10", "Order for [Name Here]", "2014-06-06",10,"Clothing", "000010", '2014-01-01', 5.00, "Status", True, True, True, "Wardrobe Item 4: Pants", '30', None, "Male", "Blue", None, 1770, 1870, "This is pants"],
    [ '50', "Middle", "Order_File11", "Liberty Boots", 22.00, "A boot from the colonial time.", "Colonial Heritage Foundation", 15.00, "ABCDEF11", "Order for [Name Here]", "2014-06-06",11,"Clothing", "000011", '2014-01-01', 5.00, "Status", True, True, True, "Wardrobe Item 5: Boots", '10', None, "Male", "Blue", None, 1770, 1870, "This is a boot"],
    [ '50', "Middle", "Order_File12", "Liberty Gloves", 22.00, "A glove from the colonial time.", "Colonial Heritage Foundation", 15.00, "ABCDEF12", "Order for [Name Here]", "2014-06-06",12,"Clothing", "000012", '2014-01-01', 5.00, "Status", True, True, True, "Wardrobe Item 6: Sword", 'M', None, "Male", "Black", None, 1770, 1870, "This is a glove"],
]:
	u = hmod.WardrobeItem()
	u.quantity_on_hand = data[0]
	u.shelf_location = data[1]
	u.order_file = data[2]

	u.name = data[3]
	u.price = data[4]
	u.description = data[5]
	u.manufacturer = data[6]
	u.average_cost  = data[7]
	u.sku = data[8]
	u.order_form_name = data[9]
	u.production_time = data[10]
	u.vendor_id = data[11]
	u.category = data[12]

	u.serial_number = [13]
	u.date_acquired = [14]
	u.cost = data[15]
	u.status = data[16]
	u.for_sale = data[17]
	u.condition_new = data[18]
	u.is_rentable = data[19]
	u.notes = data[20]

	u.size =data[21]
	u.size_modifier = data[22]
	u.gender = data[23]
	u.color =data[24]
	u.pattern =data[25]
	u.start_year = data[26]
	u.end_year =data[27]
	u.note = data[28]
	u.save()

#RentableProduct
for data in [
    [ '50', "Middle", "Order_File13", "Liberty Cannon", 122.00, "A cannon from the colonial time.", "Colonial Heritage Foundation", 30.00, "ABCDEF13", "Order for [Name Here]", "2014-06-06",13,"Weaponry", "00007", '2014-01-01', 5.00, "Status", True, True, True, "Rentable Item 1: Cannon", 5, 25.00, 100.00],
    [ '50', "Middle", "Order_File14", "Liberty Gun", 122.00, "A gun from the colonial time.", "Colonial Heritage Foundation", 30.00, "ABCDEF14", "Order for [Name Here]", "2014-06-06",14,"Weaponry", "00008", '2014-01-01', 5.00, "Status", True, True, True, "Rentable Item 2: Gun",5, 25.00, 100.00],
    [ '50', "Middle", "Order_File15", "Liberty Sword", 122.00, "A sword from the colonial time.", "Colonial Heritage Foundation", 30.00, "ABCDEF15", "Order for [Name Here]", "2014-06-06",15,"Weaponry", "00009", '2014-01-01', 5.00, "Status", True, True, True, "Rentable Item 3: Sword", 5, 25.00, 100.00],
]:
	u = hmod.RentableProduct()
	u.quantity_on_hand = data[0]
	u.shelf_location = data[1]
	u.order_file = data[2]

	u.name = data[3]
	u.price = data[4]
	u.description = data[5]
	u.manufacturer = data[6]
	u.average_cost  = data[7]
	u.sku = data[8]
	u.order_form_name = data[9]
	u.production_time = data[10]
	u.vendor_id = data[11]
	u.category = data[12]
	
	u.serial_number = [13]
	u.date_acquired = [14]
	u.cost = data[15]
	u.status = data[16]
	u.for_sale = data[17]
	u.condition_new = data[18]
	u.is_rentable = data[19]
	u.notes = data[20]

	u.times_rented = data[21]
	u.price_per_day = data[22]
	u.replacement_price = data[23]
	u.save()

#SaleItem
for data in [
   #Bulk buy of Liberty Bell by Customer1
   [ 500.00, 2, 100, 1],
   #Bulk buy of Liberty Pen by Customer2
   [ 300.00, 3, 100, 3]
]:
   u = hmod.SaleItem()
   u.price = data[0]
   u.transaction_id = data[1]
   u.quantity = data[0]
   u.item_id = data[1]
   u.save()


#Rental Item
for data in [
   #Three Guns are checked out by Patton
   [10.00, 4, '2015-01-30', '2015-02-01', '2015-02-20', None, 14],
   [10.00, 4, '2015-01-30', '2015-02-01', '2015-02-20', None, 14],
   [10.00, 4, '2015-01-30', '2015-02-01', '2015-02-20', None, 14],
   #Six Swords are checked out Washington
   [12.00, 5, '2015-01-30', '2015-02-01', '2015-02-20', None, 15],
   [12.00, 5, '2015-01-30', '2015-02-01', '2015-02-20', None, 15],
   [12.00, 5, '2015-01-30', '2015-02-01', '2015-02-20', None, 15],
   [12.00, 5, '2015-01-30', '2015-02-01', '2015-02-20', None, 15],
   [12.00, 5, '2015-01-30', '2015-02-01', '2015-02-20', None, 15],
   [12.00, 5, '2015-01-30', '2015-02-01', '2015-02-20', None, 15],

]:
   u = hmod.RentalItem()
   u.price = data[0]
   u.transaction_id = data[1]
   u.date_out = data[2]
   u.date_in = data[3]
   u.date_due = data[4]
   u.discount_percent = data[5]
   u.rentable_product_id = data[6]
   u.save()


# Fee
for data in [
    [ 1.00, False, "Late", 1],
	[ 5.00, False, "Very Late", 7],
	[ 10.00, False, "Damage", 7],
	[ 8.00, False, "Late and damaged", 13],
]:
    u = hmod.Fee()
    u.amount = data[0]
    u.waived = data[1]
    u.description = data[2]
    u.rental_product_id = data[3]
    u.save()

#select * from homepage_transaction join homepage_rentalitem  on homepage_transaction.id=homepage_rentalitem.transaction_id 
#join homepage_stockedproduct on homepage_rentalitem.rentable_product_id=homepage_stockedproduct.id join homepage_productspecification 
#on homepage_stockedproduct.product_specification_id=homepage_productspecification.id