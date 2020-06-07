from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
import datetime
import json

from . import admin
from .forms import ProductForm, CategoryForm, Codeform, EditForm
from .. import db
from ..models import Product, Purchase, User, Category, Code, Comment


def check_admin():
    if not current_user.is_admin:
        abort(403)


@admin.route('/dashboard')
@login_required
def admin_dashboard():
    check_admin()
    dic = {'Bhutan':0,'Democratic Republic of the Congo':0,'Liechtenstein':0,'Maldives':0,'Sudan':0,'Zimbabwe':0,'Mauritania':0,'Mozambique':0,'Nigeria':0,'Swaziland':0,'Tanzania':0,'Iraq':0,'Guyana':0,'Namibia':0,'Senegal':0,'Turkmenistan':0,'Afghanistan':0,'Andorra':0,'Fiji':0,'Gabon':0,'Uzbekistan':0,'Cameroon':0,'Cuba':0,'Faroe Islands':0,'El Salvador':0,'Caribbean':0,'Ethiopia':0,'Mongolia':0,'Puerto Rico':0,'Samoa':0,'Myanmar':0,'Nicaragua':0,'Seychelles':0,'Tajikistan':0,'Dominican Republic':0,'Guinea':0,'Barbados':0,'CI':0,'Laos':0,'Libya':0,'Panama':0,'Bahrain':0,'Benin':0,'Ghana':0,'Haiti':0,'Montenegro':0,'Somalia':0,'Syria':0,'Ecuador':0,'Honduras':0,'Madagascar':0,'Papua New Guinea':0,'Tunisia':0,'Angola':0,'Botswana':0,'Cyprus':0,'Algeria':0,'Bahamas':0,'New Caledonia':0,'Uganda':0,'Yemen':0,'Zambia':0,'Antarctica':0,'Paraguay':0,'Jamaica':0,'Palestine':0,'Bolivia':0,'Bosnia and Herzegovina':0,'Vietnam':0,'Kenya':0,'Luxembourg':0,'Niger':0,'Kuwait':0,'Hawaii':0,'Scotland':0,'Cambodia':0,'Uruguay':0,'Kyrgyzstan':0,'Saudi Arabia':0,'Indonesia':0,'Azerbaijan':0,'United Arab Emirates':0,'Mauritius':0,'Morocco':0,'Albania':0,'South Korea':0,'Kazakhstan':0,'Macedonia':0,'Venezuela':0,'Taiwan':0,'Qatar':0,'Jordan':0,'Iceland':0,'Guatemala':0,'Costa Rica':0,'Hong Kong':0,'San Marino':0,'Colombia':0,'Moldova':0,'Armenia':0,'Malta':0,'Nepal':0,'Lebanon':0,'Malaysia':0,'Serbia':0,'Peru':0,'Trinidad and Tobago':0,'Lithuania':0,'Estonia':0,'Georgia':0,'Iran':0,'Chile':0,'Latvia':0,'Thailand':0,'Egypt':0,'Slovenia':0,'Mexico':0,'Belarus':0,'Slovakia':0,'Sri Lanka':0,'Croatia':0,'Philippines':0,'Bangladesh':0,'Turkey':0,'Romania':0,'Italy':0,'South Africa':0,'Hungary':0,'Pakistan':0,'Portugal':0,'Ukraine':0,'Greece':0,'Oman':0,'Argentina':0,'Singapore':0,'Bulgaria':0,'Japan':0,'Czech Republic':0,'Ireland':0,'China':0,'Finland':0,'Brazil':0,'Norway':0,'Austria':0,'Denmark':0,'Belgium':0,'New Zealand':0,'Spain':0,'Switzerland':0,'Russia':0,'Poland':0,'Israel':0,'Sweden':0,'Netherlands':0,'France':0,'Australia':0,'Canada':0,'India':0,'Germany':0,'United Kingdom':0,'United States':0}
    for user in User.query.all():
        if user.addresses:
            dic[user.addresses[0].country] += 1
    listCountryMember = [['Country','Value']]
    for key in dic:
        listCountryMember.append([key, dic[key]])
    
    listNumberMember = [["Month", "Registration"]]
    listPurchaseY = [["Month", "Purchase"]]
    listPurchaseW = [["Day", "Purchase"]]
    listIncomeY = [["Month", "Income"]]
    listIncomeW = [["Day", "Income"]]
    for month in range(1,13):
        nbMember = 0
        for user in User.query.all():
            if user.subscription.month == month:
                nbMember +=1
        listNumberMember.append([str(month), nbMember])
        nbPurchaseY = 0
        nbIncomeY = 0
        for purchase in Purchase.query.all():
            if purchase.date.month == month:
                nbPurchaseY +=1
                nbIncomeY += purchase.price
        listPurchaseY.append([str(month), nbPurchaseY])
        listIncomeY.append([str(month), int(nbIncomeY)])
    for day in range(1, 8):
        nbPurchaseW = 0
        nbIncomeW = 0
        for purchase in Purchase.query.all():
            if purchase.date.day == day:
                nbPurchaseW +=1
                nbIncomeW += purchase.price
        listPurchaseW.append([str(day), nbPurchaseW])
        listIncomeW.append([str(day), int(nbIncomeW)])
    return render_template('admin/admin_dashboard.html', listNumberMember=json.dumps(listNumberMember), listCountryMember=json.dumps(listCountryMember), listPurchaseY=json.dumps(listPurchaseY), listPurchaseW=json.dumps(listPurchaseW), listIncomeY=json.dumps(listIncomeY), listIncomeW=json.dumps(listIncomeW),
                            title="Dashboard")


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
                          discount=form.discount.data,
                          image=form.image.data,
                          categories = form.categories.data,
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
                product.discount=form.discount.data
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
            product.discount=form.discount.data
            product.image = form.image.data
            product.description = form.description.data
            product.categories = form.categories.data
            db.session.commit()
            flash('You have successfully edited the product.')
            return redirect(url_for('admin.list_product'))
    form.name.data = product.name
    form.price.data = product.price
    form.discount.data = product.discount
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


@admin.route('/purchase')
@login_required
def list_purchase():
    check_admin()
    purchases = Purchase.query.all()
    return render_template('admin/purchase/purchases.html',
                           purchases=purchases, title="Purchases")

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
        form.product.data.stock += 1
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
    if not code.purchase_id:
        code.product.stock -= 1
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
        return redirect(url_for('admin.list_category'))
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
