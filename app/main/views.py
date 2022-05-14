
from flask import render_template
from app import main


@main.route('/')
def home():
    return "Home"
    