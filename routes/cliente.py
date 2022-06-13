import json
from multiprocessing.connection import Client
from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, flash, json
from pip._vendor import requests

from models.model import Arl, Cliente
from utils.db import db
import pandas as pd

cliente = Blueprint('python_cliente_routes', __name__)


@cliente.route('/show_book')
def show():
    if 'admin' in session:
        movies = Arl.all()
        return render_template('./comment/show.html', movies=movies)



@cliente.route('/delete_client/<id>')
def delete_client(id):
    if 'admin' in session:
        comment = Client.query.get(id)

        db.session.delete(comment)
        db.session.commit()
        
        return render_template('./views/Admin/cliente.html')


def get_arl():
    return Arl.query.all()

def get_arl_id(arl):
    return Arl.query.filter_by(arl = arl).first().id

def create_arl(arl_name):
    arl = Arl(arl_name)

    db.session.add(arl)
    db.session.commit()

def cont_books():
    return Arl.query.count()

def get_cliente():
    return Cliente.query.all()

def to_dict(row):
    if row is None:
        return None

    rtn_dict = dict()
    keys = row.__table__.columns.keys()
    for key in keys:
        rtn_dict[key] = getattr(row, key)
    return rtn_dict 
    
@cliente.route('/excle_cliente', methods=['GET', 'POST'])        
def exportar_cliente_excel():
    data = get_cliente()
    data_list = [to_dict(item) for item in data]
    df = pd.DataFrame(data_list)
    filename = "C:/Users/juanf/Documents/Universidad/Pr_BD/Proyecto_Final_BD_Python/export_Cliente.xlsx"
    print("Filename: "+filename)   
    
       
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer, sheet_name='Cleinte')
    writer.save()
    
    return redirect(url_for('python_admin_routes.info_cliente'))