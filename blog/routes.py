from flask import render_template, redirect, url_for, flash
from blog import app, db, bcrypt
from .forms import *
from .models import *



@app.route('/')
def home():
	return render_template('home.html')


@app.route('/sign-up', methods=['GET', 'POST'])
def signup():
	form = SignupForm()
	if form.validate_on_submit():
		hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data,
		 password=hashed_pass)
		db.session.add(user)
		db.session.commit()
		flash('Sign up seccessfully', 'success')
		return redirect(url_for('signin'))
	return render_template('signup.html', form=form)


@app.route('/sign-in')
def signin():
	form = LoginForm()
	return render_template('login.html', form=form)