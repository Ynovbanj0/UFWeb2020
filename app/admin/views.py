from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from .forms import ProductForm, CategoryForm, Codeform, EditForm
from .. import db
from ..models import Product, Purchase, User, Category, Code, Comment


def check_admin():
    if not current_user.is_admin:
        abort(403)


@admin.route('/product')
@login_required
def list_product():
    check_admin()
    products = Product.query.all()
    return render_template('admin/product/products.html',
                           products=products, title="Products")


@admin.route('/product/add', methods=['GET', 'POST'])
@login_required
def add_product():
    check_admin()
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(name=form.name.data,
                          price=form.price.data,
                          image=form.image.data,
                          description=form.description.data)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('admin.list_product'))

    return render_template('admin/product/product.html', form=form,
                           title="Add product")


@admin.route('/product/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_product(id):
    check_admin()
    product = Product.query.get_or_404(id)
    form = ProductForm(obj=product)
    if form.validate_on_submit():
        if Product.query.filter_by(name=form.name.data).first():
            if Product.query.filter_by(name=form.name.data).first().name == Product.query.filter_by(id=id).first().name:
                product.name = form.name.data
                product.price = form.price.data
                product.image = form.image.data
                product.description = form.description.data
                product.categories = form.categories.data
                db.session.commit()
                flash('You have successfully edited the product.')
                return redirect(url_for('admin.list_product'))
            else:
                flash('The product name is already taken.')
        else:
            product.name = form.name.data
            product.price = form.price.data
            product.image = form.image.data
            product.description = form.description.data
            product.categories = form.categories.data
            db.session.commit()
            flash('You have successfully edited the product.')
            return redirect(url_for('admin.list_product'))
    form.name.data = product.name
    form.price.data = product.price
    form.image.data = product.image
    form.description.data = product.description
    form.categories.data = product.categories
    return render_template('admin/product/product.html', form=form,
                           title="Edit Product")


@admin.route('/product/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_product(id):
    check_admin()
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    flash('You have successfully deleted the product.')
    return redirect(url_for('admin.list_product'))


@admin.route('/code')
@login_required
def list_code():
    check_admin()
    codes = Code.query.all()
    return render_template('admin/codes/codes.html',
                           codes=codes, title="Codes")


@admin.route('/code/add', methods=['GET', 'POST'])
@login_required
def add_code():
    check_admin()
    form = Codeform()
    if form.validate_on_submit():
        code = Code(code=form.code.data,
                    product=form.product.data)
        db.session.add(code)
        db.session.commit()
        return redirect(url_for('admin.list_code'))
    return render_template('admin/codes/code.html', form=form,
                           title="Add code")


@admin.route('/code/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_code(id):
    check_admin()
    code = Code.query.get_or_404(id)
    db.session.delete(code)
    db.session.commit()
    flash('You have successfully deleted the code.')
    return redirect(url_for('admin.list_code'))


@admin.route('/category')
@login_required
def list_category():
    check_admin()
    categories = Category.query.all()
    return render_template('admin/category/categories.html',
                           categories=categories, title="Categories")


@admin.route('/category/add', methods=['GET', 'POST'])
@login_required
def add_category():
    check_admin()
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(name=form.name.data)
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('admin.list_categories'))
    return render_template('admin/category/category.html', form=form,
                           title="Add category")


@admin.route('/category/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_category(id):
    check_admin()
    category = Category.query.get_or_404(id)
    form = CategoryForm(obj=category)
    if form.validate_on_submit():
        category.name = form.name.data
        db.session.commit()
        flash('You have successfully edited the category.')
        return redirect(url_for('admin.list_category'))
    form.name.data = category.name
    return render_template('admin/category/category.html', form=form,
                           title="Edit Category")


@admin.route('/category/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_category(id):
    check_admin()
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    flash('You have successfully deleted the category.')
    return redirect(url_for('admin.list_category'))


@admin.route('/user')
@login_required
def list_user():
    check_admin()
    users = User.query.all()
    return render_template('admin/user/users.html',
                           users=users, title="Users")


@admin.route('/user/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_user(id):
    check_admin()
    user = User.query.get_or_404(id)
    form = EditForm(obj=user)
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first() and User.query.filter_by(username=form.username.data).first():
            if User.query.filter_by(email=form.email.data).first().email == user.email and User.query.filter_by(username=form.username.data).first().username == user.username:
                user.username = form.username.data
                user.password = form.password.data
                user.email = form.email.data
                user.first_name = form.first_name.data
                user.last_name = form.last_name.data
                user.birthdate = form.birthdate.data
                db.session.commit()
                flash('You have successfully edited the profil.')
                return redirect(url_for('admin.list_user'))
            else:
                flash('Either your username or your email is already taken.')
        else:
            user.username = form.username.data
            user.password = form.password.data
            user.email = form.email.data
            user.first_name = form.first_name.data
            user.last_name = form.last_name.data
            user.birthdate = form.birthdate.data
            db.session.commit()
            flash('You have successfully edited the profil.')
            return redirect(url_for('admin.list_user'))
    return render_template('admin/user/user.html', form=form,
                           title="Edit User")


@admin.route('/user/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_user(id):
    check_admin()
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('You have successfully deleted the user.')
    return redirect(url_for('admin.list_user'))
