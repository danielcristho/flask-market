import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pasar.db'
app.config['SECRET_KEY'] = '7d1ce04a2ba2b81c2a566a04'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from market import routes
