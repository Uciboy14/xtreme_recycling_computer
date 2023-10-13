#!/bin/usr/python3
import hashlib
from base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from flask_login import UserMixin
from order import Order
import bcrypt

# Define the user model
class User(BaseModel, Base, UserMixin):
	__tablename__ = 'users'
	__table_args__ = {'extend_existing': True}  # Add this line
	
	#user_id = Column(Integer, primary_key=True)
	username = Column(String(50), unique=True, nullable=False)
	email = Column(String(100), unique=True, nullable=False)
	_password = Column(String(100), nullable=False)
	shipping_address = Column(String(200))

	# Define one-to-many relationship between user and order
	orders = relationship('Order', backref='user')

	def __init__(self, *args, **kwargs):
		"""initializes city"""
		super().__init__(*args, **kwargs)


	def check_password(self, pwd):
		password_hash = self._password
		if bcrypt.checkpw(pwd.encode(), password_hash):
			return True
		else:
			return False

	def set_password(self, password):
		"""hashing password values"""
		pwd = password
		salt = bcrypt.gensalt()
		self._password = bcrypt.hashpw(pwd.encode(), salt)

