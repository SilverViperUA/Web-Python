import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'secret'
SESSION_PERMANENT = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///D:/IT/python/lab7/instance/db.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False
