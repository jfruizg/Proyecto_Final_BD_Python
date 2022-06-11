from flask import Blueprint, render_template, request, redirect, url_for
from utils.db import db
from models.model import Empleado

empleado = Blueprint('empleado', __name__)


@empleado.route("/")
def ingreso():
    return "bienvenido"


@empleado.route("/new", methods=['POST'])
def guardar_empleado():
    id = request.form['id']
    user_id = request.form['user_id']
    nuevo_empleado = Empleado(user_id, id)
    db.session.add(nuevo_empleado)
    db.session.commit()

    return redirect("/")


@empleado.route("/delete/<id>")
def eliminar_empleado(id):
    empleado = Empleado.query.get(id)
    db.session.delete(empleado)
    db.session.commit()
    return redirect(url_for('empleado.ingreso'))


@empleado.route("/update/<id>", methods=['POST', 'GET'])
def actualizar_empleado(id):
    empleado = Empleado.query.get(id)
    if request.method == 'POST':

        empleado.id = request.form['id']
        empleado.user_id = request.form['user_id']
        db.session.commit()
        return redirect(url_for('empleado.ingreso'))

    else:

        return render_template('index.html', empleado=empleado)



def cont_empleados():
    return Empleado.query.count()