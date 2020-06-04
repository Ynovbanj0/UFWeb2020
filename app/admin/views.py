from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from .forms import ProductForm, CategoryForm, Codeform
from .. import db
from ..models import Product, Purchase, User, Category, Code, Comment


def check_admin():
    if not current_user.is_admin:
        abort(403)


@admin.route('/product')
@login_required
def list_products():
    check_admin()
    products = Product.query.all()
    return render_template('admin/products/products.html',
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
        try:
            db.session.add(product)
            db.session.commit()
        except:
            pass
        return redirect(url_for('admin.list_products'))

    return render_template('admin/products/product.html', form=form,
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
                return redirect(url_for('admin.list_products'))
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
            return redirect(url_for('admin.list_products'))
    form.name.data = product.name
    form.price.data = product.price
    form.image.data = product.image
    form.description.data = product.description
    form.categories.data = product.categories
    return render_template('admin/products/product.html', form=form,
                           title="Edit Product")


@admin.route('/product/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_product(id):
    check_admin()
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    flash('You have successfully deleted the product.')
    return redirect(url_for('admin.list_products'))


@admin.route('/code/add', methods=['GET', 'POST'])
@login_required
def add_code():
    check_admin()
    form = Codeform()
    if form.validate_on_submit():
        code = Code(code=form.code.data,
                    product=form.product.data)
        try:
            db.session.add(code)
            db.session.commit()
        except:
            pass
        return redirect(url_for('admin.list_codes'))

    return render_template('admin/codes/code.html', form=form,
                           title="Add code")


@admin.route('/code')
@login_required
def list_codes():
    check_admin()
    listCodes = []
    p = 0
    for product in Product.query.all():
        listCodes.append([product.name, []])
        for code in product.codes:
            listCodes[p][1].append(code)
        p += 1

    return render_template('admin/codes/codes.html',
                           listCodes=listCodes, title="Codes")


@admin.route('/category')
@login_required
def list_categories():
    check_admin()
    listCategories = []
    p = 0
    for category in Category.query.all():
        listCategories.append([category.name, []])
        for product in category.products:
            listCategories[p][1].append(product)
        p += 1
    return render_template('admin/categories/categories.html',
                           listCategories=listCategories, title="Categories")


@admin.route('/category/add', methods=['GET', 'POST'])
@login_required
def add_category():
    check_admin()
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(name=form.name.data)
        try:
            db.session.add(category)
            db.session.commit()
        except:
            pass
        return redirect(url_for('admin.list_categories'))

    return render_template('admin/categories/category.html', form=form,
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
        return redirect(url_for('admin.list_categories'))
    form.name.data = category.name
    return render_template('admin/categories/category.html', form=form,
                           title="Edit Category")


@admin.route('/category/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_category(id):
    check_admin()
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    flash('You have successfully deleted the category.')
    return redirect(url_for('admin.list_categories'))
