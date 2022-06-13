import json
from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, flash, json
from pip._vendor import requests

from models.model import Dependencia
from utils.db import db


dependencia = Blueprint('python_dependencia_routes', __name__)


@dependencia.route('/register_dependencia', methods=['POST','GET'])
def create():
    if 'admin' in session:
        adependencia_name = request.form["dependencia_name"]
        dependencia = Dependencia(adependencia_name)
        
        
        return redirect(url_for('python_admin_routes.info_empleado'))

@dependencia.route('/show_dependencia')
def show():
    if 'admin' in session:
        movies = Dependencia.all()
        return render_template('./comment/show.html', movies=movies)



@dependencia.route('/delete_dependencia/<id>')
def delete():
    if 'admin' in session:
        comment = Dependencia.query.get(id)

        db.session.delete(comment)
        db.session.commit()


def get_dependencia():
    return Dependencia.query.all()

def get_dependencia_id(dependencia):
    return Dependencia.query.filter_by(dependencia = dependencia).first().id

def get_dependencia_name(dependencia):
    return Dependencia.query.filter_by(id = dependencia).first().dependencia

def create_dependencia(adependencia_name):
    dependencia = Dependencia(adependencia_name)

    db.session.add(dependencia)
    db.session.commit()

def cont_dependencia():
    return Dependencia.query.count()


