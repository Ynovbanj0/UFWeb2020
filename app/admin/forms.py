from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

from ..models import Department, Role


class DepartmentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_name(self, field):
        if Department.query.filter_by(name=field.data).first():
            raise ValidationError('Department already exists.')

class RoleForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_name(self, field):
        if Role.query.filter_by(name=field.data).first():
            raise ValidationError('Role already exists.')


class EmployeeAssignForm(FlaskForm):
    department = QuerySelectField(query_factory=lambda: Department.query.all(), get_label="name")
    role = QuerySelectField(query_factory=lambda: Role.query.all(), get_label="name")
    submit = SubmitField('Submit')
