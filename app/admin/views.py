from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from .forms import DepartmentForm, EmployeeAssignForm, RoleForm
from .. import db
from ..models import Department, Employee, Role


def check_admin():
    if not current_user.is_admin:
        abort(403)


@admin.route('/departments', methods=['GET', 'POST'])
@login_required
def list_departments():
    check_admin()
    departments = Department.query.all()
    return render_template('admin/departments/departments.html',
                           departments=departments, title="Departments")


@admin.route('/departments/add', methods=['GET', 'POST'])
@login_required
def add_department():
    check_admin()
    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(name=form.name.data, 
                                description=form.description.data)
        try:
            db.session.add(department)
            db.session.commit()
        except:
            pass
        return redirect(url_for('admin.list_departments'))

    return render_template('admin/departments/department.html', action="Add",
                           add_department=True, form=form,
                           title="Add Department")


@admin.route('/departments/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_department(id):
    check_admin()
    department = Department.query.get_or_404(id)
    form = DepartmentForm(obj=department)
    if form.validate_on_submit():
        department.name = form.name.data
        department.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the department.')
        return redirect(url_for('admin.list_departments'))
    form.description.data = department.description
    form.name.data = department.name
    return render_template('admin/departments/department.html', action="Edit",
                           add_department=add_department, form=form,
                           department=False, title="Edit Department")


@admin.route('/departments/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_department(id):
    check_admin()
    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    flash('You have successfully deleted the department.')
    return redirect(url_for('admin.list_departments'))


@admin.route('/roles')
@login_required
def list_roles():
    check_admin()
    roles = Role.query.all()
    return render_template('admin/roles/roles.html',
                           roles=roles, title='Roles')


@admin.route('/roles/add', methods=['GET', 'POST'])
@login_required
def add_role():
    check_admin()
    form = RoleForm()
    if form.validate_on_submit():
        role = Role(name=form.name.data,
                    description=form.description.data)
        try:
            db.session.add(role)
            db.session.commit()
        except:
            pass
        return redirect(url_for('admin.list_roles'))
    return render_template('admin/roles/role.html', action="Add", 
                           add_role=True, form=form,
                           title='Add Role')


@admin.route('/roles/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_role(id):
    check_admin()
    role = Role.query.get_or_404(id)
    form = RoleForm(obj=role)
    if form.validate_on_submit():
        role.name = form.name.data
        role.description = form.description.data
        db.session.add(role)
        db.session.commit()
        flash('You have successfully edited the role.')
        return redirect(url_for('admin.list_roles'))
    form.description.data = role.description
    form.name.data = role.name
    return render_template('admin/roles/role.html', add_role=False,
                           form=form, title="Edit Role")


@admin.route('/roles/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_role(id):
    check_admin()
    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    flash('You have successfully deleted the role.')
    return redirect(url_for('admin.list_roles'))


@admin.route('/employees')
@login_required
def list_employees():
    check_admin()
    employees = Employee.query.all()
    return render_template('admin/employees/employees.html',
                           employees=employees, title='Employees')


@admin.route('/employees/assign/<int:id>', methods=['GET', 'POST'])
@login_required
def assign_employee(id):
    check_admin()
    employee = Employee.query.get_or_404(id)
    if employee.is_admin:
        abort(403)
    form = EmployeeAssignForm(obj=employee)
    if form.validate_on_submit():
        employee.department = form.department.data
        employee.role = form.role.data
        db.session.add(employee)
        db.session.commit()
        flash('You have successfully assigned a department and role.')
        return redirect(url_for('admin.list_employees'))
    return render_template('admin/employees/employee.html',
                           employee=employee, form=form,
                           title='Assign Employee')
