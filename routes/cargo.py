import json
from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, flash, json
from pip._vendor import requests

from models.model import Cargo
from utils.db import db


cargo = Blueprint('python_cargo_routes', __name__)


@cargo.route('/register_cargo', methods=['POST','GET'])
def create():
    if 'admin' in session:
        cargo_name = request.form["cargo_name"]

        create_cargo(cargo_name)
        
        return redirect(url_for('python_admin_routes.info_empleado'))

@cargo.route('/show_dependencia')
def show():
    if 'admin' in session:
        movies = Cargo.all()
        return render_template('./comment/show.html', movies=movies)



@cargo.route('/delete_dependencia/<id>')
def delete():
    if 'admin' in session:
        comment = Cargo.query.get(id)

        db.session.delete(comment)
        db.session.commit()


def get_cargo():
    return Cargo.query.all()

def get_cargo_id(cargo):
    return Cargo.query.filter_by(cargo = cargo).first().id
    

def cont_books():
    return Cargo.query.count()

def create_cargo(cargo_name):
    cargo = Cargo(cargo_name)

    db.session.add(cargo)
    db.session.commit()