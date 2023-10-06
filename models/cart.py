#!/bin/usr/python3
from base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from cartItem import CartItem

# Define the Cart model
class Cart(BaseModel, Base):
	__tablename__ = 'carts'
	__table_args__ = {'extend_existing': True}  # Add this line

	cart_id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('users.user_id', ondelete='CASCADE')) # Optional user: association

	# Define one-to-many relationship between Cart and CartItem
	cart_items = relationship('CartItem', backref='cart')
