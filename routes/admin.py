import json

from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, flash, json
from pip._vendor import requests
from sqlalchemy.dialects import mysql

from models.model import Empleado, Cliente, Dependencia, Cargo, Eps,Arl, Pension
from utils.db import db

admin = Blueprint('admin', __name__)

@admin.route('/info_empleado')
def info_empleados():
    if 'admin' in session:
        empleado = Empleado.all()
        nombre_empleado = empleado.user_id
        cur = mysql.connection.cursor()
        sQuery = "SELECT dependencias.dependencia FROM empleados INNER JOIN dependencias ON empleados.id_dependencia = dependencias.id; "
        cur.execute(sQuery)
        usuarios = cur.fetchone()
        cur.close()