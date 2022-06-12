from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, flash
from utils.db import db
import pandas as pd 

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