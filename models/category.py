#!/bin/usr/python3
from base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from product import Product

# Define the Category model
class Category(BaseModel, Base):
    __tablename__ = 'categories'
    __table_args__ = {'extend_existing': True}  # Add this line
    
    #category_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)

    # Define one-to-many relationship between Category and Product
    products = relationship('Product', backref='category')

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)