#!/bin/usr/python3
from base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from order import Order

# Define the user model
class User(BaseModel, Base):
	__tablename__ = 'users'

	user_id = Column(Integer, primary_key=True)
	username = Column(String(50), unique=True, nullable=False)
	email = Column(String(100), unique=True, nullable=False)
	password = Column(String(100), nullable=False)
	shipping_address = Column(String(200))

	# Define one-to-many relationship between user and order
	orders = relationship('Order', backref='user')
