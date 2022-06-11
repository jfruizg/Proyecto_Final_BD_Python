from flask import Blueprint, render_template, request, redirect, url_for
from utils.db import db
from models.model import Empleado

empleado = Blueprint('empleado', __name__)


@empleado.route("/new_employee", methods=['POST', 'GET'])
def create_emp():
    name = request.form['name']
    last_name = request.form['last_name']
    username = request.form['username']
    email = request.form['email']
    new_emp = Empleado(name, last_name, username, email)
    db.session.add(new_emp)
    db.session.commit()

    return redirect("/")


@empleado.route("/delete/<id>")
def delete_emp(id):
    empleado = Empleado.query.get(id)
    db.session.delete(empleado)
    db.session.commit()
    return redirect(url_for('empleado.ingreso'))


@empleado.route("/update/<id>", methods=['POST', 'GET'])
def update_emp(id):
    empleado = Empleado.query.get(id)
    if request.method == 'POST':

        empleado.id = request.form['id']
        empleado.user_id = request.form['user_id']
        db.session.commit()
        return redirect(url_for('empleado.ingreso'))

    else:

        return render_template('index.html', empleado=empleado)


@empleado.route("/show_emp")
def show_emp():
    empleado = Empleado.all()
    return render_template('./comment/show.html', empleado=empleado)


def cont_empleados():
    return Empleado.query.count()
