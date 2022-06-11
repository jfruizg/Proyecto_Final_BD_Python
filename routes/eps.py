import json
from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, flash, json
from pip._vendor import requests

from models.model import Eps, Pension
from utils.db import db


eps = Blueprint('python_eps_routes', __name__)


@eps.route('/register_eps', methods=['POST','GET'])
def create():
    if 'admin' in session:
        eps_name = request.form["eps_name"]

        eps = Eps(eps_name)

        db.session.add(eps)
        db.session.commit()
        
        return redirect(url_for('python_admin_routes.info_empleado'))

@eps.route('/show_pension')
def show():
    if 'admin' in session:
        movies = Eps.all()
        return render_template('./comment/show.html', movies=movies)



@eps.route('/delete_pension/<id>')
def delete():
    if 'admin' in session:
        comment = Eps.query.get(id)

        db.session.delete(comment)
        db.session.commit()



def cont_books():
    return Eps.query.count()