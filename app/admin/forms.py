from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, DecimalField, SelectMultipleField, widgets, SelectMultipleField, PasswordField, IntegerField
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField, QuerySelectField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms.fields.html5 import DateField

from ..models import Product, Category

class MultiCheckboxField(QuerySelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput() 


class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    discount = IntegerField('Discount')
    image = StringField('Image', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    categories = MultiCheckboxField('Categories', query_factory=lambda: Category.query.all(), get_label="name", validators=[DataRequired()])
    submit = SubmitField('Submit') 


class CategoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_name(self, field):
        if Category.query.filter_by(name=field.data).first():
            raise ValidationError('Category already exists.')


class Codeform(FlaskForm):
    code = StringField('Code', validators=[DataRequired()])
    product = QuerySelectField(query_factory=lambda: Product.query.all(), get_label="name")
    submit = SubmitField('Submit')


class EditForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    birthdate = DateField('Birthdate', validators=[DataRequired()], format='%Y-%m-%d')
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Update')