from flask import flash, abort, redirect, render_template, url_for, session
from flask_login import login_required, login_user, logout_user, current_user
from flask_mail import Mail, Message

from . import auth
from .forms import LoginForm, RegistrationForm, AddressForm, EditForm, CommentForm
from .. import db
from ..models import User, Address, Comment, Code, Purchase, Product
from datetime import datetime

import json


def check_user(id):
    if id != current_user.id:
        abort(403)


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
    form_ed = EditForm(obj=user)
    if form_ed.validate_on_submit():
        if User.query.filter_by(email=form_ed.email.data).first() and User.query.filter_by(username=form_ed.username.data).first():
            if User.query.filter_by(email=form_ed.email.data).first().email == current_user.email and User.query.filter_by(username=form_ed.username.data).first().username == current_user.username:
                user.username = form_ed.username.data
                user.password = form_ed.password.data
                user.email = form_ed.email.data
                user.first_name = form_ed.first_name.data
                user.last_name = form_ed.last_name.data
                user.birthdate = form_ed.birthdate.data
                db.session.commit()
                flash('You have successfully edited the profil.')
            else:
                flash('Either your username or your email is already taken.')
        else:
            user.username = form_ed.username.data
            user.password = form_ed.password.data
            user.email = form_ed.email.data
            user.first_name = form_ed.first_name.data
            user.last_name = form_ed.last_name.data
            user.birthdate = form_ed.birthdate.data
            db.session.commit()
            flash('You have successfully edited the profil.')
    return render_template('auth/profil.html', form_ed=form_ed, user=user,
                           title="Profil")


@auth.route('/address/add', methods=['GET', 'POST'])
@login_required
def add_address():
    form = AddressForm()
    if form.validate_on_submit():
        address = Address(address=form.address.data,
                          city=form.city.data,
                          postal=form.postal.data,
                          country=form.country.data,
                          user_id=current_user.id)
        db.session.add(address)
        db.session.commit()
        return redirect(url_for('auth.profil'))
    return render_template('auth/address/address.html', form=form,
                           title="Add address")


@auth.route('/address/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_address(id):
    address = Address.query.get_or_404(id)
    check_user(address.user_id)
    form = AddressForm(obj=address)
    if form.validate_on_submit():
        address.address = form.address.data
        address.city = form.city.data
        address.postal = form.postal.data
        address.country = form.country.data
        db.session.commit()
        flash('You have successfully edited the address.')
        return redirect(url_for('auth.profil'))
    form.address.data = address.address
    form.city.data = address.city
    form.postal.data = address.postal
    form.country.data = address.country
    return render_template('auth/address/address.html', form=form,
                           title="Edit Address")


@auth.route('/address/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_address(id):
    address = Address.query.get_or_404(id)
    check_user(address.user_id)
    db.session.delete(address)
    db.session.commit()
    flash('You have successfully deleted the address.')
    return redirect(url_for('auth.profil'))


@auth.route('/comment/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_comment(id):
    comment = Comment.query.get_or_404(id)
    check_user(address.user_id)
    form = CommentForm(obj=comment)
    if form.validate_on_submit():
        comment.content = form.content.data
        comment.rating = form.rating.data
        db.session.commit()
        flash('You have successfully edited the comment.')
        return redirect(url_for('auth.profil'))
    form.content.data = comment.content
    form.rating.data = comment.rating
    return render_template('auth/comment/comment.html', form=form,
                           title="Edit Comment")


@auth.route('/comment/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_comment(id):
    comment = Comment.query.get_or_404(id)
    check_user(address.user_id)
    db.session.delete(comment)
    db.session.commit()
    flash('You have successfully deleted the comment.')
    return redirect(url_for('auth.profil'))


@auth.route('/purchase')
@login_required
def purchase():
    purchase = Purchase(price= int(session['total']) / 100,
                        date = datetime.now(),
                        user_id = current_user.id)
    db.session.add(purchase)
    for id in session['productsId']:
        purchase.codes.append(Code.query.filter_by(product_id=id).filter_by(purchase_id=None).first())
        purchase.products.append(Product.query.filter_by(id=id).first())
        db.session.commit()
    # Send mail to User with purchase
    msg = Message('You\'r purchase(s) at No Play No Play !', recipients=[current_user.email])
    mail.send(msg)
    return redirect(url_for('auth.profil'))
