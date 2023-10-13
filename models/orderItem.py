#!/bin/usr/python3
from base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Numeric, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from product import Product

# Define the OrderItem model
class OrderItem(BaseModel, Base):
	__tablename__ = 'order_items'
	__table_args__ = {'extend_existing': True}  # Add this line
	
	#order_item_id = Column(Integer, primary_key=True)
	order_id = Column(Integer, ForeignKey('orders.id', ondelete='CASCADE'), nullable=False)
	product_id = Column(Integer, ForeignKey('products.id', ondelete='CASCADE'), nullable=False)
	quantity = Column(Integer, nullable=False)
	unit_price = Column(Numeric(precision=10, scale=2), nullable=False)

	# Define many-to-one relationship between OrderItem and Order
	#order = relationship('Order', back_populates='order_items')
	# Define many-to-one relationship between OrderItem and Product
	#product = relationship('Product', back_populates='order_items')

	def __init__(self, *args, **kwargs):
		"""initializes city"""
		super().__init__(*args, **kwargs)