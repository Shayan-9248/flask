from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo



class SignupForm(FlaskForm):
	username = StringField('Username',
	 validators=[DataRequired(), Length(min=4, max=27)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm_Password',
	 validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign-up')


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember_me')