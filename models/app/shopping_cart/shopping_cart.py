#!/bin/usr/python3
from user import User
from models.cartItem import CartItem
from models.cart import CartItem
from models.product import Product

product = Product()
items = CartItem()

# Method to add a product to the cart
def addToCart(product):
	# Check if the product is already in the cart
	if product.id is in items:
		# Update the quantity 
		existingItem = getItemProductID(productID)
		existingItem.quantity = existingItem.quantity + quantity
	else:
		# Create a new cart item
		newItem = CartItem(productID, productName, productPrice, quantity)
		self.items.append(newItem)""


# Method to remove a product from the cart
def removeFromCart(productID):
	""" Remove the item with productID from items """
	for item in items:
		if item.productID == productID:
			# Remove the item from the cart
			items.










