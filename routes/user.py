import json

from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, flash, json
from pip._vendor import requests

from models.model import User, Admin, Empleado, Cliente, Dependencia, Cargo, Eps,Arl, Pension
from utils.db import db

user = Blueprint('user', __name__)
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
        return render_template('./user/index.html', contacts=user)
    else:
        delete_message = 'Hasta luego'
        flash(delete_message)
        return render_template('./user/register.html', sitekey=sitekey)


@user.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('python_contact_routes.home'))

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

        new_user = User(name, password, last_name,user_tipe, username)

        db.session.add(new_user)
        db.session.commit()

        user = User.query.filter_by(username=username).first()
        user_id = user.id


        if(user_tipe == 1):
            new_admin = Admin(user_id)
            data_base_add(new_admin)
            session['admin'] = username
        elif(user_tipe == 2):
            new_empleado = Empleado(user_id)
            data_base_add(new_empleado)
            session['username'] = username
        elif(user_tipe == 3):
            new_cliente = Cliente(user_id)
            data_base_add(new_cliente)
            session['username'] = username



        return redirect(url_for('python_contact_routes.home'))
    else:
        return render_template('./user/register.html', sitekey=sitekey)

@user.route('/cookie')
def cookie():
    response = make_response(render_template("./user.cookies.html"))
    response.set_cookie('custome_cookie', 'Eduardo')
    return response

def data_base_add(aux):
    db.session.add(aux)
    db.session.commit()



