from flask import abort, render_template, session
from flask_login import current_user, login_required
from datetime import datetime

from . import home
from .. import db
from .forms import CommentForm
from ..models import *

import json

@home.route('/')
def homepage():
    nbItem = len(session['productsId'])
    total = session['total'] / 100
    return render_template('home/index.html', total=total, nbItem=nbItem, title="Welcome")


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


@home.route('/cart/add/<int:id>', methods=['GET', 'POST'])
@login_required
def add_cart(id):
    return "Comming Soon"


@home.route('/product/<int:id>', methods=['GET', 'POST'])
def product(id):
    product = Product.query.get_or_404(id)
    sum = 0
    count = 0
    for comment in product.comments:
        sum += comment.rating
        count += 1
    if sum:
        rating = round(sum/count, 1)
    else:
        rating = 0
    form = CommentForm()
    if form.validate_on_submit():
        if Comment.query.filter_by(user_id=current_user.id).first():
            comment.content = form.content.data
            comment.rating = form.rating.data
            product.rating = rating
            db.session.commit()
        else:
            comment = Comment(content=form.content.data,
                              date=datetime.now(),
                              rating=form.rating.data,
                              user_id=current_user.id,
                              product_id=id)
            product.rating = rating
            db.session.add(comment)
            db.session.commit()
    user_comment = Comment.query.filter_by(user_id=current_user.id).first()
    if user_comment:
        form.content.data = user_comment.content
        form.rating.data = user_comment.rating
    return render_template('home/product/product.html', product=product, form=form, user=current_user, rating=rating, title="Product")


@home.route('/categories')
def list_categories():
    categories = Category.query.all();
    nbItem = len(session['productsId'])
    total = session['total'] / 100 
    return render_template('home/categories.html',
                           categories=categories, total=total, nbItem=nbItem, title="Categories")


@home.route('/category/<name>')
def category(name):
    category = Category.query.filter_by(name=name).first()
    nbItem = len(session['productsId'])
    total = session['total'] / 100
    # seeTotal = session['total']
    # seeId = session['productsId']
    return render_template('home/category.html', 
                           category=category, total=total, nbItem=nbItem, title=category.name)


@home.route('/addToCard/<int:id>')
def addToCard(id):
    # On récupère l'objet du produit ajouté au panier
    product = Product.query.filter_by(id=id).first()
    productId = [product.id]
    # On peut pas stocké un type decimal en session
    productPrice = int(product.price * 100)
    # On créer un total a update en vérifiant que session['total'] existe sinon set a 0
    if session['total'] != None :
        session['total'] = session['total'] + productPrice
    else :
        session['total'] = 0
        session['total'] = session['total'] + productPrice
    # On créer une liste a update en vérifiant que session['productsId'] existe sinon set a vide
    if session['productsId'] != None :
        tempProdId = session['productsId'] 
        tempProdId = tempProdId + productId
        session['productsId'] = tempProdId
    else :
        session['productsId'] = []
        tempProdId = session['productsId'] 
        tempProdId = tempProdId + productId
        session['productsId'] = tempProdId
    message = '{ "message":"Card Updated" }'
    return json.loads(message)
