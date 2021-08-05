from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pasar.db'
db = SQLAlchemy(app)

from market import routes
from market import db

db.create_all()