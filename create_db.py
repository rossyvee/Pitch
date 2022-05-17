import os
from app import db,create_app
# from flask_migrate import migrate
app=create_app('production')
# app.config['SQLALCHEMY_DATABASE_URI']='postgres://ugwvtsmiuritaa:dda5ba73451268789df57d15662955dbb69d15119135639cb8c4dafccfd13208@ec2-54-172-175-251.compute-1.amazonaws.com:5432/dep65eldusiv8i'
db.init_app(app)

with app.app_context():
    db.create_all()


