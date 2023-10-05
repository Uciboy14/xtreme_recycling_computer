#!/bin/usr/python3
from base_model import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey

# Define the Brand model
class Brand(BaseModel, Base):
    __tablename__ = 'brands'

    brand_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)

    # Define one-to-many relationship between Brand and Product
    products = relationship('Product', back_populates='brand')
