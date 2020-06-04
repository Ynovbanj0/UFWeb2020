from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user, current_user

from . import auth
from .forms import LoginForm, RegistrationForm, AddressForm, EditForm
from .. import db
from ..models import User, Address


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    password=form.password.data,
                    email=form.email.data,
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    birthdate=form.birthdate.data)
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
    addresses = Address.query.filter_by(id=current_user.id).all()
    form_ed = EditForm(obj=user)
    form_add = AddressForm()
    if form_ed.validate_on_submit():
        if User.query.filter_by(email=form_ed.email.data).first() or User.query.filter_by(username=form_ed.username.data).first():
            if User.query.filter_by(email=form_ed.email.data).first().email == current_user.email and User.query.filter_by(username=form_ed.username.data).first().username == current_user.username:
                user.username=form_ed.username.data
                user.password=form_ed.password.data
                user.email=form_ed.email.data
                user.first_name=form_ed.first_name.data
                user.last_name=form_ed.last_name.data
                user.birthdate=form_ed.birthdate.data
                db.session.commit()
                flash('You have successfully edited the profil.')
            else:
                flash('Either your username or your email is already taken.')
        else:
            user.username=form_ed.username.data
            user.password=form_ed.password.data
            user.email=form_ed.email.data
            user.first_name=form_ed.first_name.data
            user.last_name=form_ed.last_name.data
            user.birthdate=form_ed.birthdate.data
            db.session.commit()
            flash('You have successfully edited the profil.')
    if form_add.validate_on_submit():
        address = Address(city=form_add.city.data,
                          postal=form_add.postal.data,
                          country=form_add.country.data,
                          address=form_add.address.data,
                          user_id=current_user.id)
        db.session.add(address)
        db.session.commit()
    return render_template('auth/profil.html', form_ed=form_ed, form_add=form_add,
                           title="Profil")

    