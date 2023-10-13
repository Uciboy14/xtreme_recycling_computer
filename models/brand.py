#!/bin/usr/python3
from base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


# Define the Brand model
class Brand(BaseModel, Base):
    __tablename__ = 'brands'
    __table_args__ = {'extend_existing': True}  # Add this line
    
    #brand_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)

    # Define one-to-many relationship between Brand and Product
    products = relationship('Product', backref='brand')

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
