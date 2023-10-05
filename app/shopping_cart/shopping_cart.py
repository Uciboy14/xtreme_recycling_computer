#!/bin/usr/python3
from user import User

class ShoppingCart:
	# Attributes
	items = []
	cartTotal = 0
	user = User()

def __init__(self):
	self.user = user
	self.items = []


# Method to add a product to the cart
def addToCart(self, productID, productName, productPrice, quantity):
	# Check if the product is already in the cart
	if productID is in items:
		# Update the quantity 
		existingItem = getItemProductID(productID)
		existingItem.quantity = existingItem.quantity + quantity
	else:
		# Create a new cart item
		newItem = CartItem(productID, productName, productPrice, quantity)
		self.items.append(newItem)


# Method to remove a product from the cart
def removeFromCart(productID):
	""" Remove the item with productID from items """
	for item in items:
		if item.productID == productID:
			# Remove the item from the cart
			items.










