
from flask import render_template, redirect, url_for,abort,request
from . import main
from flask_login import login_required,current_user
from ..models import User,Pitch,Comment,Upvote,Downvote
from .forms import UpdateProfile,PitchForm,CommentForm
from .. import db


@main.route('/')
def home():
    pitches = Pitch.query.all()
    business = Pitch.query.filter_by(category = 'Job').all() 
    technology = Pitch.query.filter_by(category = 'Events').all()
    idea = Pitch.query.filter_by(category = 'Advertisement').all()
    return render_template('index.html', business = business,technology = technology, pitches = pitches,idea= idea)
