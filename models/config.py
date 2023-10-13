#!/bin/usr/python3

import os
base_dir = os.path.abspath(os.path.dirname(__file__))
print(base_dir)

# Configure the path for the SQLite database
db_filename = 'myshop.db'  # Your database filename
db_path = os.path.join(base_dir, db_filename)

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard_to_guess_string'
	MAIL_SERVER = os.environ.get('MAIL_SERVER', 'daviduciboy@gmail.com')
	MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
	MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
	FLASK_MAIL_SENDER = 'Flasky Admin <daviduciboy@gmail.com>'
	FLASK_ADMIN = os.environ.get('FLASKY_ADMIN')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True 
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or f'sqlite:///{db_path}'

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or 'sqlite://'

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')


config = {
'development': DevelopmentConfig,
'testing': TestingConfig,
'production': ProductionConfig, 
'default': DevelopmentConfig
	}



