#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import sys
from pathlib import Path
base_dir = Path(__file__).parent.parent
sys.path.append(str(base_dir))

#import models
from base_model import BaseModel, Base
from user import User
from order import Order
from product import Product
from category import Category
from cartItem import CartItem
from brand import Brand
from discount import Discount
from cart import Cart
from payment import Payment
from orderItem import OrderItem
import os
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import IntegrityError

classes = {'user': User, 'product': Product, 'order': Order, 'category': Category, 'cartitem': CartItem, 'brand': Brand, 'discount': Discount, 'cart': Cart, 'orderitem': OrderItem, 'payment': Payment}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        MYSQL_USER = os.getenv('MYSQL_USER')
        MYSQL_PWD = os.getenv('MYSQL_PWD')
        MYSQL_HOST = os.getenv('MYSQL_HOST')
        MYSQL_DB = os.getenv('MYSQL_DB')
        MYSQL_ENV = os.getenv('MYSQL_ENV')
        DIALECT = os.getenv('DIALECT')
        DRIVER = os.getenv('DRIVER')

        if  MYSQL_ENV == 'test':
            self.__engine = create_engine("mysql+mysqlconnector://hbnb_dev:four1cup@127.0.0.1/hbnb_dev_db", pool_pre_ping=True)
            Base.metadata.create_all(self.__engine)
            sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
            Session = scoped_session(sess_factory)
            self.__session = Session

        else:
            print("Using dev Environment")
            self.__engine = create_engine('sqlite:///../xtreme_recycling_computer.db')
            Base.metadata.create_all(self.__engine)
            sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
            Session = scoped_session(sess_factory)
            self.__session = Session

    def all(self, cls=None):
        """query on the current database session"""
        # Import your model classes here to ensure they're recognized by SQLAlchemy

        if cls is None:
            classes = [Customer, Product, Category, CartItem, Order]
        else:
            classes = [cls]

        result = {}
        with self.__session() as session:
            for model_class in classes:
                objects = session.query(model_class).all()
                for obj in objects:
                    result[f"{obj.__class__.__name__}.{obj.id}"] = obj
        return result


    def new(self, obj):
        """add the object to the current database session"""
        try:
            self.__session.add(obj)
        except IntegrityError as e:
            self.__session.rollback()
            print('Integrity Error ', e)
        except Exception as e:
            self.__session.rollback()
            print('Exception Occured: ', e)

    def save(self):
        """commifout all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls=None, id=None):
        """Returns obj based on class name and its ID"""
        if cls is not None and id is not None:
            try:
                retrieved_customer = self.__session.query(classes[cls]).get(id)
                if retrieved_customer is None:
                    print("Customer not found.")
                else:
                    print("Retrieved Customer:", retrieved_customer)
                    return retrieved_customer
            except Exception as e:
                print("An error occurred:", str(e))
        return None

    def count(self, cls=None):
        """Returns the amount of objects"""
        if cls is not None:
            try:
                return len(self.all(classes[cls]))
            except:
                return None
        else:
            return len(self.all())
