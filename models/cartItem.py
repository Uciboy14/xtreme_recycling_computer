#!/bin/usr/python3
from base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


# Define the CartItem model
class CartItem(BaseModel, Base):
	__tablename__ = 'cart_items'

	cart_item_id = Column(Integer, primary_key=True)
	cart_id = Column(Integer, ForeignKey('carts.cart_id', ondelete='CASCADE'), nullable=False)
	product_id = Column(Integer, ForeignKey('products.product_id', ondelete= 'CASCADE'), nullable=False)
	quantity = Column(Integer, nullable=False)

	# Define many-to-one relationship between CartItem and Cart
	#cart = relationship('Cart', back_populates='cart_items')
	# Define many-to-one relatioship between CartItem and Product
	#product = relationship('Product', back_populates='cart_items')
