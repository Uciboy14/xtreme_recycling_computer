#!/bin/usr/python3
import os
import sys

from pathlib import Path

base_dir = Path(__file__).parent.parent
print(base_dir)
sys.path.append(str(base_dir))


from flask_login import LoginManager
from flask import Flask
from config import config
from flask_bootstrap import Bootstrap
#flask_mail import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


bootstrap = Bootstrap()
#mail = Mail()
#moment = Moment()
#db = storage

#def create_app(config_name):
app = Flask(__name__)
app.config.from_object(config['default'])
config['default'].init_app(app)
#migrate = Migrate(app, db)
#db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = 'user.login'
login_manager.init_app(app)
bootstrap.init_app(app)
#mail.init_app(app)

#attach routes and custom error pages here
from app.users.user import user_bp
#from app.auth.auth import auth_bp
#from app.admin.admin import admin_bp
app.register_blueprint(user_bp)
#app.register_blueprint(admin_bp)
#app.register_blueprint(auth_bp)
#return app

