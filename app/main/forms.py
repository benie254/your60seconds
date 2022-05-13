from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, StringField, SelectField
from wtforms.validators import InputRequired


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[InputRequired()])
    submit = SubmitField('Update Profile')


class PitchForm(FlaskForm):
    pitch_title = StringField('Title')
    pitch_content = TextAreaField('Content')
    pitch_category = SelectField('Category', choices=['sales', 'entertainment', 'love', 'uncategorized', 'job'])
    submit = SubmitField('Submit Pitch')


class CommentForm(FlaskForm):
    message = TextAreaField('What are your thoughts on this?')
    submit = SubmitField('Share Comment')

