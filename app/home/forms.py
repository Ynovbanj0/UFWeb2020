from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, IntegerField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, NumberRange
from flask_login import current_user

from ..models import Product, Address
    
class CommentForm(FlaskForm):
    content = StringField('Content')
    rating = IntegerField('Rating', validators=[NumberRange(min=0, max=5)])
    submit = SubmitField('Submit')

class AddressForm(FlaskForm):
    address = QuerySelectField(query_factory=lambda: Address.query.filter_by(user_id=current_user.id).all(), get_label="address")
    submit = SubmitField('Submit')
