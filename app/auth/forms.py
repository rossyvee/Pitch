from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from ..models import User

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired
()])
    category = SelectField('Category', choices=[('Events','Events'),('Job','Job'),('Advertisement','Advertisement')],validators=[DataRequired
()])
    post = TextAreaField('Your Pitch', validators=[DataRequired
()])
    submit = SubmitField('Pitch')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.',validators = [DataRequired
()])
    submit = SubmitField('Save')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[DataRequired
()])
    submit = SubmitField('Comment')
