import json

from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, flash, json
from pip._vendor import requests
from sqlalchemy import false, true
from sqlalchemy.dialects import mysql

from models.model import Empleado, Admin, EmpleadoNomina,Dependencia,Arl,Cargo,Pension,Eps
from routes.author import all_authors
from routes.publicadores import all_publicadores
from utils.db import db
from routes.arl import get_arl
from routes.cargo import get_cargo
from routes.empleado import get_empleados, cont_empleados
from routes.dependencia import get_dependencia
from routes.pension import get_pension
from routes.eps import eps, get_eps

admin = Blueprint('python_admin_routes', __name__)

        
def all_admin():
    return Admin.query.all() 

@admin.route('/info_empleado')
def info_empleado():
    if admin_insesssion():
        arl = get_arl()
        pension = get_pension()
        eps = get_eps()
        dependencia = get_dependencia()
        cargo = get_cargo()
        empleados = get_empleados()
        
        results = db.session.query(Empleado,EmpleadoNomina,Dependencia,Arl,Cargo,Pension,Eps).join(Empleado,Dependencia,Arl,Cargo,Pension,Eps)
        
    
        return render_template("./views/Admin/empleado.html",all_empleados = empleados ,all_arl = arl, all_pension = pension, all_cargo= cargo, all_dependencia = dependencia, all_eps=eps, nomina_empleado = results)
    else:
        return render_template("./views/Admin/index.html")
    
@admin.route('/info_pelicula')
def info_pelicula():
    if admin_insesssion():
        return render_template('./views/Admin/peliculaadmin.html')
    else:
        return render_template("./views/Admin/index.html")
    
@admin.route('/info_libro')
def info_libro():
    authors = all_authors()
    publicadores = all_publicadores()
    
    if admin_insesssion():
        return render_template('./views/Admin/libroadmin.html', empleados = cont_empleados() ,all_author = authors, all_publicadores=publicadores)
    else:
        return render_template("./views/Admin/index.html")     
    
@admin.route('/info_dato')
def info_dato():
    if admin_insesssion():
        return render_template('./views/Admin/datos.html')
    else:
        return render_template("./views/Admin/index.html")       



def admin_insesssion():
    if 'admin' in session: 
        return true
    else:
        return false
    