import json

from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, flash, json
from pip._vendor import requests
from sqlalchemy import false, true
from sqlalchemy.dialects import mysql

from models.model import Autor, Empleado, Libro,Genre,Admin, EmpleadoNomina,Dependencia,Arl,Cargo, Pelicula,Pension,Eps, Publicador
from routes.author import all_authors
from routes.publicadores import all_publicadores
from utils.db import db
from routes.arl import get_arl
from routes.cargo import get_cargo
from routes.empleado import get_empleados, cont_empleados
from routes.dependencia import get_dependencia , get_dependencia_name
from routes.pension import get_pension
from routes.eps import eps, get_eps
from routes.genre import all_genre


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
        cont = (cont_nomina_empleado())
        
        results_dep = []
        ids = []
        
        for i in cont:
            for j in i:
                results_dep.append(db.session.query(EmpleadoNomina,Dependencia).join(Dependencia).filter(Dependencia.id == j).count())
                dependencia = Dependencia.query.filter_by(id = j).first().dependencia
                ids.append(dependencia)
        
        
        result = convert(ids, results_dep)   
        print(result)
        labels = [row[0] for row in result]
        values = [row[1] for row in result]
       
        
    
        return render_template("./views/Admin/empleado.html",all_empleados = empleados ,all_arl = arl, all_pension = pension, all_cargo= cargo, all_dependencia = dependencia, all_eps=eps, nomina_empleado = results, labels=labels, values=values)
    else:
        return render_template("./views/Admin/index.html")
    
@admin.route('/info_pelicula')
def info_pelicula():
    if admin_insesssion():
        
        genres = Genre.query.all()
        
        print(genres)
        results = db.session.query(Pelicula,Genre).join(Genre)
        
        return render_template('./views/Admin/peliculadmin.html', all_genre = all_genre(), movies = results)
    else:
        return render_template("./views/Admin/index.html")
    
@admin.route('/info_libro')
def info_libro():
    authors = all_authors()
    publicadores = all_publicadores()
    
    results = db.session.query(Libro,Autor,Publicador).join(Autor,Publicador)
    
    if admin_insesssion():
        return render_template('./views/Admin/libroadmin.html', empleados = cont_empleados() ,all_author = authors, all_publicadores=publicadores, tabla = results)
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
    
def cont_nomina_empleado():
    id = db.session.query(Dependencia.id)
    all_ids = id.all()
    return all_ids

def convert(*args):
    """
    Returns a list of tuples generated from multiple lists and tuples
    """
    for x in args:
        if not isinstance(x, list) and not isinstance(x, tuple):
            return []

    size = float("inf")
    
    for x in args:
        size = min(size, len(x))
        
    result = []
    
    for i in range(size):
        result.append(tuple([x[i] for x in args]))
        
    return result