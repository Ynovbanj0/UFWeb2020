from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, IntegerField
from wtforms.validators import DataRequired, NumberRange

from ..models import Product
    
class CommentForm(FlaskForm):
    content = StringField('Content')
    rating = IntegerField('Rating', validators=[NumberRange(min=0, max=5)])
    submit = SubmitField('Submit')