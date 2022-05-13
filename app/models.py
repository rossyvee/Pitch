# model class for user
#model class for categories
#model  class for pitches
#models class for votes
#model class for comments
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)