#!/bin/usr/python3
from base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Numeric, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from orderItem import OrderItem


# Define the Order model
class Order(BaseModel, Base):
	__tablename__ = 'orders'
	__table_args__ = {'extend_existing': True}  # Add this line
	
	#order_id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE')) #Optional User: association
	order_date = Column(DateTime(timezone=True), default=datetime.now(), nullable=False)
	total_price = Column(Numeric(precision=10, scale=2), nullable=False)
	shipping_address = Column(String(200), nullable=False)
	status = Column(String(20), nullable=False)

	# Define one-to-many relationship between Order and OrderItem
	order_items = relationship('OrderItem', backref='order')
	# Defie many-to-one relationship between Order and User
	#user = relationship('User', back_populates='orders')

	def __init__(self, *args, **kwargs):
		"""initializes city"""
		super().__init__(*args, **kwargs)
