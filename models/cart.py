#!/bin/usr/python3
from base_model import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey

# Define the Cart model
class Cart(BaseModel, Base):
	__tablename__ = 'carts'

	cart_id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('users.user_id', ondelete='CASCADE')) # Optional user: association

	# Define one-to-many relationship between Cart and CartItem
	cart_items = relationship('CartItem', back_populates='cart')
