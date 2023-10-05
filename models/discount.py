#!/bin/usr/python3
from base_model import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey

# Define the Discount model
class Discount(BaseModel, Base):
    __tablename__ = 'discounts'

    discount_id = Column(Integer, primary_key=True)
    code = Column(String(20), unique=True, nullable=False)
    percentage = Column(Integer, nullable=False)
    expiration_date = Column(DateTime(timezone=True))