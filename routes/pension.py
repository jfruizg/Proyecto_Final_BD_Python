import json
from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, flash, json
from pip._vendor import requests

from models.model import Dependencia, Pension
from utils.db import db


pension = Blueprint('python_pension_routes', __name__)


@pension.route('/register_pension', methods=['POST','GET'])
def create():
    if 'admin' in session:
        pension_name = request.form["pension_name"]

        pension = Pension(pension_name)

        db.session.add(pension)
        db.session.commit()
        
        return redirect(url_for('python_admin_routes.info_empleado'))

@pension.route('/show_pension')
def show():
    if 'admin' in session:
        movies = Pension.all()
        return render_template('./comment/show.html', movies=movies)



@pension.route('/delete_pension/<id>')
def delete():
    if 'admin' in session:
        comment = Pension.query.get(id)

        db.session.delete(comment)
        db.session.commit()


def get_pension():
    return Pension.query.all()

def get_pension_id(pension):
    return Pension.query.filter_by(pension = pension).first().id

def cont_books():
    return Pension.query.count()