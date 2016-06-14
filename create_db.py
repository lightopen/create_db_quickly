# create_db_quickly
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
# database name
db_name = 'zbolg.sqlite'
unix = "sqlite:////"
windows = "sqlite:///"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = unix + os.path.join(basedir, da_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


# models.py

 

