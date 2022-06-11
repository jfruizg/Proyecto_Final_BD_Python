import imp
import json


from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, flash, json
from pip._vendor import requests
from sqlalchemy import false, true

from routes.empleado import guardar_empleado, cont_empleados
from routes.admin import all_admin
from routes.book import cont_books
from routes.movie import cont_movies
from models.model import Empleado, Cliente, Admin
from utils.db import db



user = Blueprint('python_user_routes', __name__)
sitekey = "6LcnlUUgAAAAAA0QSZbLaxs5zyjXsBwC0JqML1-G"

def is_human(captcha_response):
    """ Validating recaptcha response from google server
        Returns True captcha test passed for submitted form else returns False.
    """

    #privada
    secret = "6LcnlUUgAAAAAP_3tDNsNJRht5dXvcypfwUlWD40"
    payload = {'response':captcha_response, 'secret':secret}
    response = requests.post("https://www.google.com/recaptcha/api/siteverify", payload)
    response_text = json.loads(response.text)
    return response_text['success']


@user.route('/')
def home():
    #se coloca la publica
    if 'username' in session:
        username = session['username']
        print(username)
        success_message = 'Bienvenido {}'.format(username)
        flash(success_message)
        return render_template('./views/User/login.html', sitekey=sitekey)
    elif 'client' in session:
        client = session['client']
        print(client)
        return render_template('./views/User/login.html')
    elif 'admin' in session:
        username_admin = session['admin']
        admin_insession = Admin.query.filter_by(username = username_admin)
        admins = all_admin()
        
    
        return render_template('./views/Admin/index.html', admin = admin_insession, empleados = cont_empleados(), clientes = cont_clientes(), libros = cont_books(), peliculas = cont_movies())
    else:
        delete_message = 'Hasta luego'
        flash(delete_message)
        return render_template('./views/User/Registro.html', sitekey=sitekey)


@user.route('/log')
def log():
    return render_template('./views/User/login.html')

@user.route('/admin_empleado')
def empleado():
    return render_template('./views/Admin/empleado.html')

@user.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    elif 'admin' in session:
        session.pop('admin')
    elif 'client' in session:
        session.pop('client')

    return redirect(url_for('python_user_routes.home'))

@user.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if user is not None and user.verify_password(password):
        session['username'] = username
        return redirect(url_for('python_contact_routes.home'))
    else:
        return redirect(url_for('python_contact_routes.home'))

@user.route('/register', methods=['POST','GET'])
def register():
    username_admin = request.form['username_admin']
    captcha_response = request.form['g-recaptcha-response']
    if(username_admin != ""):
        if is_human(captcha_response):
            name = request.form['nombre_admin']
            last_name = request.form['apellido_admin']
            correo  = request.form['correo_admin']
            
            session['admin'] = username_admin
             
            admin = Admin(username_admin,name,last_name,correo)
            
            db.session.add(admin)
            db.session.commit()
        
            return redirect(url_for('python_user_routes.home'))
        else:
            print("aca estoy")
            return render_template('./views/User/Login.html', sitekey=sitekey)
    else:
        print("aca perdido estoy")
        return render_template('./views/User/Login.html', sitekey=sitekey)

@user.route('/cookie')
def cookie():
    response = make_response(render_template("./user.cookies.html"))
    response.set_cookie('custome_cookie', 'Eduardo')
    return response

def cont_clientes():
    return Cliente.query.count()

def get_user_id(username):
    user_id = user.id
    return user_id



     
    





