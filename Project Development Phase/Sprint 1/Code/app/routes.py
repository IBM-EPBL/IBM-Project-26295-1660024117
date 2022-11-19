from flask import render_template, flash, request, url_for, redirect, session,  get_flashed_messages
from app import app, mail, db
from app.forms import RegistrationForm
from app.models import User
from passlib.hash import sha256_crypt


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
			return redirect('dashboard.html')
		return render_template('register.html', form=form)
	except Exception as e:
		return render_template('error.html',e=e)