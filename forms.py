from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, TextAreaField, SubmitField,RadioField
from wtforms.validators import DataRequired
from wtforms import validators, validationError

class ContactForm(FlaskForm):
	name=TextField("Name of student",[validators.Required("Please enter your name")])
	Gender=RadioField('Gender', choices)