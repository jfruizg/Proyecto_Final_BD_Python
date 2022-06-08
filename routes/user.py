import json

from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, flash, json
from pip._vendor import requests

from models.model import User, Admin, Empleado, Cliente, Dependencia, Cargo, Eps,Arl, Pension
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
        user = User.query.filter_by(username=username).first()
        success_message = 'Bienvenido {}'.format(username)
        flash(success_message)
        return render_template('./views/User/login.html', sitekey=sitekey)
    elif 'client' in session:
        client = session['client']
        print(client)
        return render_template('./views/User/login.html')
    elif 'admin' in session:
        admin = session['admin']
        print(admin)
        return render_template('./views/Admin/index.html')
    else:
        delete_message = 'Hasta luego'
        flash(delete_message)
        return render_template('./views/User/Registro.html', sitekey=sitekey)


@user.route('/log')
def log():
    return render_template('./views/User/login.html')

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

    user = User.query.filter_by(username=username).first()
    if user is not None and user.verify_password(password):
        session['username'] = username
        return redirect(url_for('python_contact_routes.home'))
    else:
        return redirect(url_for('python_contact_routes.home'))

@user.route('/register', methods=['POST'])
def register():


    name = request.form['name']
    last_name = request.form['last_name']
    username = request.form['username']
    password = request.form['password']
    captcha_response = request.form['g-recaptcha-response']
    user_tipe = request.form['user_tipe']

    if is_human(captcha_response):

        if(user_tipe == "Administrador"):
            data_base_add(name, password, last_name, 1, username)
            user_id = get_user_id(username)
            add_empleado(user_tipe,user_id)
            session['admin'] = username
        elif(user_tipe == "Empleado"):
            data_base_add(name, password, last_name, 2, username)
            user_id = get_user_id(username)
            add_empleado(user_tipe,user_id)
            session['username'] = username
        elif(user_tipe == "Cliente"):
            data_base_add(name, password, last_name, 3, username)
            user_id = get_user_id(username)
            add_empleado(user_tipe,user_id)
            session['client'] = username

        return redirect(url_for('python_user_routes.home'))
    else:
        return render_template('./views/User/Registro.html', sitekey=sitekey)

@user.route('/cookie')
def cookie():
    response = make_response(render_template("./user.cookies.html"))
    response.set_cookie('custome_cookie', 'Eduardo')
    return response

def data_base_add(name, password, last_name, user_tipe, username):
    new_user = User(name, password, last_name, user_tipe, username)

    db.session.add(new_user)
    db.session.commit()

def add_empleado(user_tipe,user_id):

    if(user_tipe == 1):
        new_empleado = Admin(user_id)
        db.session.add(new_empleado)
        db.session.commit()

    elif(user_tipe == 2):
        new_empleado = Empleado(user_id)
        db.session.add(new_empleado)
        db.session.commit()

    elif(user_tipe == 3):
        new_empleado = Cliente(user_id)
        db.session.add(new_empleado)
        db.session.commit()

def get_user_id(username):
    user = User.query.filter_by(username=username).first()
    user_id = user.id
    return user_id



