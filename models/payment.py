#!/bin/usr/python3
from base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Numeric, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from order import Order

# Define the Payment model
class Payment(BaseModel, Base):
	__tablename__ = 'payments'

	payment_id = Column(Integer, primary_key=True)
	order_id = Column(Integer, ForeignKey('orders.order_id', ondelete='CASCADE'), nullable=False)
	payment_date = Column(DateTime(timezone=True), default=datetime.now(), nullable=False)
	payment_status = Column(String(20), nullable=False)
	payment_method = Column(String(20), nullable=False)
	transaction_id = Column(String(50))

	# Define one-to-one relationship Payment and Order
	order = relationship('Order', uselist=False, backref='payments')
	 
