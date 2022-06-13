import json
from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, flash, json
from pip._vendor import requests

from models.model import Autor, Publicador
from utils.db import db


publicador = Blueprint('python_publicador_routes', __name__)


@publicador.route('/register_publicador', methods=['POST','GET'])
def create():
    if 'admin' in session:
        name = request.form["publicador_name"]
        
        create_book(name)
        return redirect(url_for('python_admin_routes.info_libro'))

@publicador.route('/show_publicador')
def show():
    if 'admin' in session:
        movies = Publicador.all()
        return render_template('./comment/show.html', movies=movies)



@publicador.route('/delete_pension/<id>')
def delete():
    if 'admin' in session:
        comment = Publicador.query.get(id)

        db.session.delete(comment)
        db.session.commit()



def all_publicadores():
    return Publicador.query.all()

def get_publicadores_id(name):
    return Publicador.query.filter_by(name = name).first().id

def cont_books():
    return Publicador.query.count()

def create_publicador(name):
    publicador = Publicador(name)

    db.session.add(publicador)
    db.session.commit()