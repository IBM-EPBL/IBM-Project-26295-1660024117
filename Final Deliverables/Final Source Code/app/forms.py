from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField	
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError


class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators=[DataRequired()]) 
	password = PasswordField('Password', validators=[DataRequired()])
	confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])


class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
