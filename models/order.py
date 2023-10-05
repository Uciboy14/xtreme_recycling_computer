#!/bin/usr/python3
from base_model import BaseModel
from sqlalchemy import Column, String, Integer, Numeric, ForeignKey, DateTime

# Define the Order model
class Order(BaseModel, Base):
	__tablename__ = 'orders'

	order_id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('users.user_id', ondelete='CASCADE')) #Optional User: association
	order_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
	total_price = Column(Numeric(precision=10, scale=2), nullable=False)
	shipping_address = Column(String(200), nullable=False)
	status = Column(String(20), nullable=False)

	# Define one-to-many relationship between Order and OrderItem
	order_items = relationship('OrderItem', back_populates='order')
	# Defie many-to-one relationship between Order and User
	user = relationship('User', back_populates='orders')
