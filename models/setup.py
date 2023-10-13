import os
from base_model import BaseModel
from brand import Brand
from user_ import User
from category import Category
from order import Order
from orderItem import OrderItem
from payment import Payment
from discount import Discount
from product import Product
from cart import CartItem
from cartItem import CartItem
from engine.db_storage import DBStorage

print("**********ADMIN DASHBOARD************\n")
print("[1]){}\n[2]{}\n[3]{}\n[4]{}\n[5]{}\n[6]{}\n[7]{}\n[8]{}\n[9]{}\n[10]{}\n".format(
	'User','CartItem','Cart','Category','Product',
	'Discount','Payment','Order',
	'OrderItem','Brand', ))

storage = DBStorage()
opt = int(input('=> '))

if opt == 1:
	def user():
		print("***********USER************\n")
		os.system('clear')
elif opt == 2:
	def cartitem():
		print("***********CART ITEM************\n")
		os.system('clear')

elif opt == 3:
	def cart():
		print("***********CART************\n")
		os.system('clear')

elif opt == 4:
	def category():
		os.system('clear')
		print("***********CATEGORY************\n")
		print("[1]){}\n[2]{}\n[3]{}\n[4]{}\n[5]{}\n[6]{}\n".format('CREATE', 'READ', 'UPDATE', 'DELETE', 'GET', 'COUNT'))
		opt = int(input('=> '))

		if opt == 1:
			print("\nCategory Name\n")
			name = input('=> ')

			if name != "":
				print('\n*******STORE WHEN NAME NOT EMPTY******')
				obj = storage.all()
				for key, value in obj.items():
					print(key, value, '\n')

				cat = {'name': name}
				category = Category(**cat)
				print(category.to_dict())
				category.save()

				print('\n*******STORE WHEN NAME NOT EMPTY******')
				obj = storage.all()
				for key, value in obj.items():
					print(key, value, '\n')
			else:
				print('\n**********STORE WHEN NAME EMPTY******')
				obj = storage.all()
				for key, value in obj.items():
					print(key, value, '\n')

	category()

elif opt == 5:
	def product():
		os.system('clear')
		print("***********PRODUCT************\n")
		print("[1]){}\n[2]{}\n[3]{}\n[4]{}\n[5]{}\n[6]{}\n".format('CREATE', 'READ', 'UPDATE', 'DELETE', 'GET', 'COUNT'))
		opt = int(input('=> '))
		print("Apple BrandID: '099fa01a-a353-4e73-9714-9ae90d8c4a45',\nLenovo BrandID: 'ef9b1cf7-01ec-414a-97c9-d1b5e7c46efc'\nHP BrandID: 'ecf2fe70-9e45-41d2-b4a9-5a08c501ae0c'\nDELL BrandID: 'ac04502f-848b-4fa7-b34f-2b382e2be307'\nIBM BrandId: '5d500419-f7ac-4a56-9daf-a30fcc3e0757'\nSAMSUNG BrandID: '5de45b52-734c-4d73-8af2-1a1ff7220895'\n")
		print('Laptop CategoryID: 0027a10f-2246-410b-9fda-e814920c12e4')
		product = {}
		if opt == 1:
			print("\nCategory Name\n")

			time =  int(input("How many times you wanna go: "))
			for i in range(time):
				product['name'] = input("Name: ")
				product['description'] = input("Description: ")
				product['price'] = float(input("Price: "))
				product['stock_quantity'] = int(input("Quantity: "))
				product['image_urls'] = input("Image Path: ")
				product['brand_id'] = input("Brand ID: ")
				product['category_id'] = input("Category ID: ")

				print("\n", product)

				p = Product(**product)
				p.save()

	product()

elif opt == 6:
	def discount():
		print("***********DISCOUNT************\n")
		os.system('clear')

elif opt == 7:
	def payment():
		print("***********PAYMENT************\n")
		os.system('clear')

elif opt == 8:
	def order():
		print("***********ORDER************\n")
		os.system('clear')

elif opt == 9:
	def orderitem():
		print("***********ORDER ITEM************\n")
		os.system('clear')

elif opt == 10:
	def brand():
		os.system('clear')
		print("***********BRAND************\n")

		print("[1]){}\n[2]{}\n[3]{}\n[4]{}\n[5]{}\n[6]{}\n".format('CREATE', 'READ', 'UPDATE', 'DELETE', 'GET', 'COUNT'))
		opt = int(input('=> '))

		if opt == 1:
			print("\nBrand Name\n")
			name = input('=> ')

			if name != "":
				print('\n*******STORE WHEN NAME NOT EMPTY******')
				obj = storage.all()
				for key, value in obj.items():
					print(key, value, '\n')


				bra = {'name': name}
				brand = Brand(**bra)
				obj = storage.all()
				for key, value in obj.items():
					print(key, value, '\n')

				brand.save()

				print('\n*******STORE WHEN NAME NOT EMPTY******')
				print(storage.all() ,'\n')
			else:
				print('\n**********STORE WHEN NAME EMPTY******')
				obj = storage.all()
				for key, value in obj.items():
					print(key, value, '\n')

	brand()
else:
	print("Wrong Option!")
