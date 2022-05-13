from flask import render_template
from app import app

@main.route('/')
def index():
    pitches = Pitch.query.all()
    product = Pitch.query.filter_by(category = 'product').all() 
    technology = Pitch.query.filter_by(category = 'techology').all()
    business = Pitch.query.filter_by(category = 'business').all()
    return render_template('index.html', product = product,business = business, pitches = pitches,technology= technology)
