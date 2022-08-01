from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '4156e3619c604634022d31aba05b3060'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#app.config['SECRET_KEY']= getenv('SECRET_KEY')
#app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")

db = SQLAlchemy(app)

from application import routes