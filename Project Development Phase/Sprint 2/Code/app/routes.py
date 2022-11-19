from flask import render_template, flash, request, url_for, redirect, session,  get_flashed_messages
from app import app, mail, db
from app.forms import RegistrationForm, LoginForm
from app.models import User, Budget, Category, Expenditure 
from passlib.hash import sha256_crypt
from functools import wraps
import random
import gc, os


def already_logged_in(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			flash("You are already logged in!", "success")
			return redirect(url_for('dashboard'))
		else:
			return f(*args, **kwargs)
	return wrap

def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args,**kwargs)
		else:
			flash('You need to login first!', "warning")
			return redirect(url_for('login_page'))
	return wrap

@app.route('/', methods=['GET','POST'])
def main():
	return render_template('main.html')

@app.route('/logout/')
@login_required
def logout():
	flash("You have been logged out!", "success")
	session.clear()
	gc.collect()
	return redirect(url_for('main'))

@app.route('/login/', methods=['GET','POST'])
@already_logged_in
def login_page():
	try:
		form = LoginForm(request.form)
		if request.method == 'POST':
			_username = form.username.data
			_password = form.password.data
			if verify(_username, _password) is False:
				return render_template('login.html', form=form)
			session['logged_in'] = True
			session['username'] = _username
			gc.collect()
			return redirect(url_for('dashboard'))
			
		return render_template('login.html', form=form)
	except Exception as e:
		return render_template('error.html',e=e)

@app.route('/register/', methods=['GET','POST'])
def register_page():
	try:
		print('break1')
		form = RegistrationForm(request.form)
		if request.method == 'POST':
			print('break2')
			_username = form.username.data
			_email = form.email.data
			_password = sha256_crypt.encrypt(str(form.password.data))
			user = User(username = _username, email = _email, password = _password)
			print('break-----456')
			if User.query.filter_by(username=_username).first() is not None:
				flash('User Already registered with username {}'.format(User.query.filter_by(username=_username).first().username), "warning")
				return render_template('register.html', form=form)
			if User.query.filter_by(email=_email).first() is not None:
				flash('Email is already registered with username {}'.format(User.query.filter_by(email=_email).first().username), "warning")
				return render_template('register.html', form=form)	
			flash("Thank you for registering!", "success")
			print('break3')
			db.session.add(user)
			db.session.commit()
			db.session.close()
			gc.collect()
			print('break4')
			session['logged_in'] = True
			session['username'] = _username
			session.modified = True
			print('break5')
			return redirect(url_for('dashboard'))
		return render_template('register.html', form=form)
	except Exception as e:
		return render_template('error.html',e=e)