import json

from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, flash, json
from pip._vendor import requests
from sqlalchemy import false, true
from sqlalchemy.dialects import mysql

from models.model import Empleado, Admin
from routes.author import all_authors
from routes.publicadores import all_publicadores
from utils.db import db

admin = Blueprint('python_admin_routes', __name__)

        
def all_admin():
    return Admin.query.all() 

@admin.route('/info_empleado')
def info_empleado():
    if admin_insesssion():
        return render_template("./views/Admin/empleado.html")
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
        return render_template('./views/Admin/libroadmin.html', all_author = authors, all_publicadores=publicadores)
    else:
        return render_template("./views/Admin/index.html")        



def admin_insesssion():
    if 'admin' in session: 
        return true
    else:
        return false
    