#!/bin.usr/python3
import os
import sys
from pathlib import Path
base_dir = Path(__file__).parent
print(base_dir)
sys.path.append(str(base_dir))


from engine.db_storage import DBStorage
storage = DBStorage()
storage.reload()


