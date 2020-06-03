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
    rating = sum / count
    form = CommentForm()
    if form.validate_on_submit():
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
    return render_template('home/product.html', product=product, form=form, user=current_user, rating=rating, title="Product")