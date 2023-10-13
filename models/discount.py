#!/bin/usr/python3
from base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

# Define the Discount model
class Discount(BaseModel, Base):
    __tablename__ = 'discounts'
    __table_args__ = {'extend_existing': True}  # Add this line
    
    #discount_id = Column(Integer, primary_key=True)
    code = Column(String(20), unique=True, nullable=False)
    percentage = Column(Integer, nullable=False)
    expiration_date = Column(DateTime(timezone=True))

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)