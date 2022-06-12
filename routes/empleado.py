from flask import Blueprint, render_template, request, redirect, url_for
from routes.pension import get_pension_id
from utils.db import db
from models.model import Empleado, EmpleadoNomina
from routes.arl import get_arl, get_arl_id
from routes.cargo import get_cargo, get_cargo_id
from routes.dependencia import get_dependencia, get_dependencia_id
from routes.eps import eps, get_eps_id


empleado = Blueprint('python_empleado_routes', __name__)


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


@empleado.route("/register_nomina", methods=['POST', 'GET'])
def create_empleado_nomina():
    empleado_id = get_empleado_id(request.form['empleado_id'])
    arl_id = get_arl_id(request.form['arl_id'])
    cargo_id = get_cargo_id(request.form['cargo_id'])
    eps_id = get_eps_id(request.form['eps_id']) 
    dependencia_id = get_dependencia_id(request.form['dependencia_id'])
    pension_id = get_pension_id(request.form['pension_id'])
    
  
    new_emp_nomina = EmpleadoNomina(empleado_id, dependencia_id, cargo_id, eps_id, arl_id, pension_id)
    db.session.add(new_emp_nomina)
    db.session.commit()

    return redirect(url_for('python_admin_routes.info_empleado'))

@empleado.route("/delete_emp/<id>")
def delete_emp(id):
    empleado = Empleado.query.get(id)
    db.session.delete(empleado)
    db.session.commit()
    return redirect(url_for('python_admin_routes.info_empleado'))


@empleado.route("/update_emp/<id>", methods=['POST', 'GET'])
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


def get_empleados():
    return Empleado.query.all()

def get_empleado_id(empleado):
    return Empleado.query.filter_by(username = empleado).first().id