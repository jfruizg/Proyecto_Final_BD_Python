from MySQLdb import IntegrityError
from flask import Blueprint, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from routes.pension import create_pension, get_pension_id
from utils.db import db
from models.model import Empleado, EmpleadoNomina
from routes.arl import get_arl, get_arl_id, create_arl
from routes.cargo import get_cargo, get_cargo_id, create_cargo
from routes.dependencia import get_dependencia, get_dependencia_id, create_dependencia
from routes.eps import eps, get_eps_id, create_eps
import pandas as pd


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


@empleado.route("/show_data")
def show_data():
    return render_template('./views/datos.html')

@empleado.route('/data', methods=['POST', 'GET'])
def data():
    if request.method == 'POST':
        file = request.form["upload_excel_file"]
        data = pd.read_excel(file)

     
        valores = data.values
        cont = 5     
        crear_datos_empleado(valores)
        for row in valores:
            cont = cont + 1
            codigo = row[0]
            nombre = row[1]
            dependencia = (row[2])
            cargo = (row[3])
            eps = (row[5])
            arl = (row[6])
            pension = (row[7])
            username = f"empleado {codigo}"
            correo = f"empleado {codigo}@gmail.com"
            
            create_empleado(nombre,username,correo,codigo)
            create_empleado_nomina( get_empleado_id(username), get_dependencia_id(dependencia), get_cargo_id(cargo), get_eps_id(eps), get_arl_id(arl), get_pension_id(pension))
           
        
        return render_template("./views/Admin/datos.html")


    return render_template("./views/Admin/datos.html")

def create_data(cargo,eps,arl,dependencia,pension):
    create_cargo(cargo)
    create_eps(eps)
    create_arl(arl)
    create_dependencia(dependencia)
    create_pension(pension)
    
    
def create_empleado_nomina(empleado_id, dependencia_id, cargo_id, eps_id, arl_id, pension_id):
    new_emp_nomina = EmpleadoNomina(empleado_id, dependencia_id, cargo_id, eps_id, arl_id, pension_id)
    db.session.add(new_emp_nomina)
    db.session.commit()
    
def create_empleado(nombre_completo,username_empleado,correo,codigo):
    empleado = Empleado(nombre_completo,username_empleado,correo,codigo)
            
    db.session.add(empleado)
    db.session.commit() 
  
def data_crear_cargo(variable):
    for i in variable:
        create_cargo(i)
        
def data_crear_eps(variable):
    for i in variable:
        create_eps(i)

def data_crear_arl(variable):
    for i in variable:
        create_arl(i)        
        
def data_crear_dependencia(variable):
    for i in variable:
        create_dependencia(i) 
      
def data_crear_pension(variable):
    for i in variable:
        create_pension(i)                  
    
def crear_datos_empleado(valores):
    dependencia = []
    cargo = []
    eps = []
    arl = []
    pension = []
    for row in valores:
        dependencia.append(row[2])
        cargo.append(row[3])
        eps.append(row[5])
        arl.append(row[6])
        pension.append(row[7])
    
    
    data_crear_cargo(list(set(arl)))
    data_crear_arl(list(set(arl)))
    data_crear_dependencia(list(set(dependencia)))
    data_crear_eps(list(set(eps)))
    data_crear_pension(list(set(dependencia)))    