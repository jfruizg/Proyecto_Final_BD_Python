#blueprint es una forma de conectar los archivos a la base de datos
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_session_captcha import FlaskSessionCaptcha
from app import recaptcha

"""
En esta variable se guarda el nombre el cual se va representar el Blueprint en app.py
"""
example = Blueprint('example', __name__)
"""
En este archvio se va a crear metodos del back para la funcion del prog

Se usa el example el cual esta conectado alarchivo inicial por medio del blue print

"/" - este es el nonmbre como se va mostrar la ruta en la aplicacion

"""

@example.route("/", methods=['POST', 'GET'])
def home():
    return render_template("./User/login.html")


@example.route('/submit', methods=['POST'])
def submit():
    if recaptcha.verify():
        flash('New Device Added successfully')
        return redirect(url_for('register'))
    else:
        flash('Error ReCaptcha')
        return redirect(url_for('register'))