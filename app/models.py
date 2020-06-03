from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


categories_products = db.Table('categories_products',
                               db.Column('category_id', db.Integer, db.ForeignKey(
                                   'categories.id'), primary_key=True),
                               db.Column('product_id', db.Integer, db.ForeignKey(
                                   'products.id'), primary_key=True)
                               )


class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    products = db.relationship('Product',
                               secondary=categories_products, lazy='subquery',
                               back_populates="categories")

    def __repr__(self):
        return "<Category: {}>".format(self.name)


class Code(db.Model):
    __tablename__ = "codes"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    def __repr__(self):
        return "<Code: {}>".format(self.code)


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    date = db.Column(db.DateTime, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    def __repr__(self):
        return '<Comment: {}>'.format(self.content)


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    price = db.Column(db.Numeric(5, 2))
    image = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    comments = db.relationship('Comment',
                               backref='product', lazy='dynamic')
    purchases = db.relationship('Purchase',
                                backref='product', lazy='dynamic')
    codes = db.relationship('Code',
                            backref='product', lazy='dynamic')
    categories = db.relationship('Category',
                                 secondary=categories_products, lazy='subquery',
                                 back_populates="products")
                                 
    def __repr__(self):
        return '<Product: {}, {}>'.format(self.name, self.description)


class Purchase(db.Model):
    __tablename__ = 'purchases'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    price = db.Column(db.Numeric(5, 2), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    code = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    def __repr__(self):
        return '<Purchase: {}, {}>'.format(self.name, self.price)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    birthdate = db.Column(db.DateTime, nullable=False)
    address = db.Column(db.String(255))
    is_admin = db.Column(db.Boolean, default=False)
    comments = db.relationship('Comment', backref='user',
                               lazy='dynamic')
    purchases = db.relationship('Purchase', backref='user',
                                lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))