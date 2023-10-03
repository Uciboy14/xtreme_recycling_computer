#!/bin.usr/python3
import os
import sys


working_path = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(working_path)
sys.path.append(parent_dir)
from models.engine.db_storage import DBStorage
storage = DBStorage()
#storage.reload()

