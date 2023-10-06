#!/bin/usr/python3
from base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

# Define the Category model
class Category(BaseModel, Base):
    __tablename__ = 'categories'

    category_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)

    # Define one-to-many relationship between Category and Product
    products = relationship('Product', backref='category')