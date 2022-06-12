from flask import Blueprint, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from routes.pension import create_pension, get_pension_id
from utils.db import db
from models.model import Cliente, EmpleadoNomina
import pandas as pd

cliente = Blueprint('python_cliente_routes',__name__)

@cliente.route("/new_client", methods=['POST', 'GET'])
def create_client():
    name = request.form['name']
    last_name = request.form['last_name']
    email = request.form['email']
    username = request.form['username']
    address = request.form['address']
    phone = request.form['phone']
    new_cli = Cliente(name,last_name,email,username,address,phone)
    db.session.add(new_cli)
    db.session.commit()
    return redirect("cliente.html")


