import imp
import json


from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, flash, json
from pip._vendor import requests
from sqlalchemy import false, true

from routes.empleado import cont_empleados
from routes.admin import all_admin
from routes.book import cont_books
from routes.movie import cont_movies

import pandas as pd
from models.model import Empleado, Cliente, Admin
from utils.db import db



data = Blueprint('python_data_routes', __name__)

@data.route('/data', methods=['POST', 'GET'])
def data():
    if request.method == 'POST':
        file = request.form["upload_excel_file"]
        print(file)
        data = pd.read_excel(file)

        lista = []
        valores = data.values
        for row in valores:
            username = row[0]
            email = row[1]
            pasw = row[2]
            
        return render_template("./views/Admin/datos.html", data = lista)


    return render_template()