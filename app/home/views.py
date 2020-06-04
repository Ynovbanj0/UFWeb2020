from flask import abort, render_template
from flask_login import current_user, login_required
from datetime import datetime

from . import home
from .. import db
from .forms import CommentForm
from ..models import *


@home.route('/')
def homepage():
    return render_template('home/index.html', title="Welcome")


@home.route('/dashboard')
@login_required
def dashboard():
    return render_template('home/dashboard.html', title="Dashboard")


@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        abort(403)
    return render_template('home/admin_dashboard.html', title="Dashboard")


@home.route('/product/<int:id>', methods=['GET', 'POST'])
def product(id):
    product = Product.query.get_or_404(id)
    sum = 0
    count = 0
    for comment in product.comments:
        sum += comment.rating
        count +=1
    rating = round(sum/count, 1)
    form = CommentForm()
    if form.validate_on_submit():
        if Comment.query.filter_by(user_id=current_user.id).first():
            comment.content = form.content.data
            comment.rating = form.rating.data
            db.session.commit()
        else:
            comment = Comment(content=form.content.data,
                            date=datetime.now(),
                            rating=form.rating.data,
                            user_id=current_user.id,
                            product_id=id)
        try:
            db.session.add(comment)
            db.session.commit()
        except:
            pass
    if Comment.query.filter_by(user_id=current_user.id).first():
        form.content.data = comment.content
        form.rating.data = comment.rating
    return render_template('home/product.html', product=product, form=form, user=current_user, rating=rating, title="Product")


@home.route('/categories')
def list_categories():
    categories = []
    p = 0
    for category in Category.query.all():
        categories.append([category.name, []])
        for product in category.products:
            categories[p][1].append(product)
        p += 1
    return render_template('home/categories.html',
                           categories=categories, title="Categories")

@home.route('/categories/<name>')
def category(name):
    category = Category.query.filter_by(name=name).first()
    return render_template('home/category.html', category=category, title=category.name)