from flask import abort, render_template, session, redirect, url_for, request
from flask_login import current_user, login_required
from sqlalchemy.sql.expression import func
from datetime import datetime
from decimal import Decimal

from . import home
from .. import db
from .forms import CommentForm
from ..models import *

import json


def checksession():
    # Function tchecking if session variable is set or sets it to 0
    if 'productsId' in session:
        nbItem = len(session['productsId'])
        session['nbItem'] = nbItem
    else:
        session['productsId'] = []
        session['nbItem'] = 0
    if 'total' in session:
        total = int(session['total']) / 100
    else:
        session['total'] = 0
        total = 0
    return total


@home.route('/')
def homepage():
    total = checksession()
    # Query to get 10 newest products
    newProducts = Product.query.order_by(Product.id.desc()).limit(10)
    popularProducts = Category.query.filter_by(name="Favorite").first()
    return render_template('home/index.html', newProducts=newProducts, popularProducts=popularProducts, total=total, title="Welcome")


@home.route('/search', methods=['GET', 'POST'])
def search():
    total= checksession()
    # Getting the GET form data, False if there is nothing there so it doesn't crash
    tag = request.args.get("s", False)
    # formatting data to put it in a like query
    search = "%{}%".format(tag)
    # Query to get all products with a name like the GET data
    searchProd = Product.query.filter(Product.name.like(search)).all()
    return render_template('home/search.html', searchProd=searchProd, total=total, title="Search")


@home.route('/product/<int:id>', methods=['GET', 'POST'])
def product(id):
    total = checksession()
    # Getting products with id in url or 404 if id doesn't exist 
    product = Product.query.get_or_404(id)
    sum = 0
    count = 0
    # Get the average rating for a product
    for comment in product.comments:
        sum += comment.rating
        count += 1
    if sum:
        rating = round(sum/count, 1)
    else:
        rating = 0
    # The add comment form for the connected user
    form = CommentForm()
    if form.validate_on_submit():
        if Comment.query.filter_by(user_id=current_user.id).filter_by(product_id=id).first():
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
    try:
        user_comment = Comment.query.filter_by(user_id=current_user.id).first()
    except:
        user_comment = None
    if user_comment:
        form.content.data = user_comment.content
        form.rating.data = user_comment.rating
    return render_template('home/product/product.html', product=product, form=form, user=current_user, total=total,
                           title="Product")


@home.route('/categories')
def list_category():
    total = checksession()
    categories = Category.query.all()
    return render_template('home/category/categories.html',
                           categories=categories, total=total, title="Categories")


@home.route('/category/<name>')
def category(name):
    total = checksession()
    category = Category.query.filter_by(name=name).first().name
    return render_template('home/category/category.html',
                           category=category, total=total, title=category)


@home.route('/addToCard/<int:id>')
def addToCard(id):
    product = Product.query.filter_by(id=id).first()
    productId = [product.id]
    productPrice = int(product.price * 100)
    if session['total'] != None:
        total = int(session['total']) + productPrice
        session['total'] = str(total)
    else:
        session['total'] = 0
        session['total'] = session['total'] + productPrice
    if session['productsId'] != None:
        tempProdId = session['productsId']
        tempProdId = tempProdId + productId
        session['productsId'] = tempProdId
    else:
        session['productsId'] = []
        tempProdId = session['productsId']
        tempProdId = tempProdId + productId
        session['productsId'] = tempProdId
    message = '{ "message":"Card Updated" }'
    return "json.loads(message)"


@home.route('/comment/delete/<int:id_com>/<int:id_prod>', methods=['GET', 'POST'])
@login_required
def delete_comment(id_com, id_prod):
    if not current_user.is_admin:
        abort(403)
    comment = Comment.query.get_or_404(id_com)
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('home.product', id=id_prod))


@home.route('/card')
@login_required
def card():
    card = []
    total = checksession()
    index = 0
    if 'productsId' in session:
        nbItem = len(session['productsId'])
    else:
        session['productsId'] = []
        nbItem = 0
    while index < nbItem:
        tempProd = session['productsId'][index]
        product = Product.query.filter_by(id=tempProd).first()
        card.append(product)
        index += 1
    return render_template('/home/card.html', card=card, total=total, title="Card")


@home.route('/deleteCard/<int:id>')
def deleteFromCard(id):
    # we get the product into databse
    product = Product.query.filter_by(id=id).first()
    # We find he's index in the list
    index = session['productsId'].index(id)
    # we delete it from the list
    session['productsId'].pop(index)
    # update the total of card
    tempTotal = int(session['total']) - int(product.price * 100)
    session['total'] = str(tempTotal)
    # update the number of articles in the card
    tempNumber = int(session['nbItem']) - 1
    session['nbItem'] = str(tempNumber)
    message = '{ "message":"Card Updated" }'
    return "json.loads(message)"


@home.route('/gimmeYourBankAccount')
@login_required
def yumyum():
    return render_template('/home/yumyum.html', title="No Pay ?")
