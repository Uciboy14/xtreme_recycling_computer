#/bin/usr/python3
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import IntegrityError
import os
import sys

#from cartitem import CartItem
#from order import Order
#from category import Category
#from product import Product
#from base_model import BaseModel, Base


working_path = os.getcwd()
work_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(work_dir)
sys.path.append(parent_dir)


print(work_dir)

time_format = "%Y-%m-%dT%H:%M:%S.%f"

Base = declarative_base()

class BaseModel:
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                    if "id" not in kwargs:
                        self.id = str(uuid4())
                    elif "created_at" not in kwargs:
                        self.created_at = self.updated_at = datetime.utcnow()
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
                    
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)


    def to_dict(self):
        obj_dict = self.__dict__.copy()
        if "__sa_instance_state" in obj_dict:
            obj_dict.pop("_sa_instance_state")
        for key, value in self.__dict__.items():
              if key in ("created_at", "updated_at"):
                obj_dict[key] = value.isoformat()
        obj_dict["__class__"] = self.__class__.__name__

        return obj_dict

    def save(self):
        from models import storage
        try:
            self.updated_at = datetime.utcnow()
            storage.new(self)
            storage.save()
        except IntegrityError as e:
            print('Integrity Error: ', e)
        except Exception as e:
            print(e)

    def delete(self):
        models.storage.delete()

    
        
