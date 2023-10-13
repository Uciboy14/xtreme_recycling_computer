#!/bin/usr/python3
from base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from brand import Brand
from cartItem import CartItem

# Define the product model
class Product(BaseModel, Base):
	__tablename__ = 'products'
	__table_args__ = {'extend_existing': True}  # Add this line
	
	#product_id = Column(Integer, primary_key=True)
	name = Column(String(100), nullable=False)
	description = Column(String(200))
	price = Column(Numeric(precision=10, scale=2), nullable=False)
	stock_quantity = Column(Integer, nullable=False)
	image_urls = Column(String(200))
	# Add foreign keys to Brand and Category
	brand_id = Column(Integer, ForeignKey('brands.id'))
	category_id = Column(Integer, ForeignKey('categories.id'))

	# Define many-to-one relationships between Product and Brand/Category
	#brand = relationship('Brand', back_populates='products')
	#category = relationship('Category', back_populates='products')
	# Define one-to-many relationship between Product and CartItem
	cart_items = relationship('CartItem', backref='product')
	# Define many-to-one relationship between Product and OrderItem
	#order_items = relationship('OrderItem', back_populates='product')

	def __init__(self, *args, **kwargs):
		"""initializes city"""
		super().__init__(*args, **kwargs)