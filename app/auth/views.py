from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user, current_user

from . import auth
from .forms import LoginForm, RegistrationForm
from .. import db
from ..models import User


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
<<<<<<< HEAD
        user = User(email=form.email.data,
                            username=form.username.data,
                            first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            password_hash=form.password.data
                            # birthdate=form.birthdate.data
                            # address=form.address.data
        )
=======
        user = User(username=form.username.data,
                    password=form.password.data,
                    email=form.email.data,
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    address=form.address.data,
                    birthdate=form.birthdate.data)
>>>>>>> d88ceed2bce76c2e92b5daa6e91e66a44cab63f4
        db.session.add(user)
        db.session.commit()
        # flash('You have successfully registered! You may now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form, title='Register')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(
                form.password.data):
            login_user(user)
            if user.is_admin:
                return redirect(url_for('home.admin_dashboard'))
            else:
                return redirect(url_for('home.homepage'))
        else:
            flash('Invalid email or password.')
    return render_template('auth/login.html', form=form, title='Login')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully been logged out.')
    return redirect(url_for('auth.login'))


@auth.route('/profil', methods=['GET', 'POST'])
@login_required
def profil():
    user = User.query.get_or_404(current_user.id)
    form = RegistrationForm(obj=user)
    if form.validate_on_submit():
        user.username=form.username.data
        user.password=form.password.data
        user.email=form.email.data
        user.first_name=form.first_name.data
        user.last_name=form.last_name.data
        user.address=form.address.data
        user.birthdate=form.birthdate.data
        db.session.commit()
        flash('You have successfully edited the profil.')
        if user.is_admin:
            return redirect(url_for('home.admin_dashboard'))
        else:
            return redirect(url_for('home.dashboard'))
    form.username.data = user.username
    form.email.data = user.email
    form.first_name.data = user.first_name
    form.last_name.data = user.last_name
    form.address.data = user.address
    form.birthdate.data = user.birthdate
    return render_template('auth/profil.html', form=form,
                           title="Profil")

    