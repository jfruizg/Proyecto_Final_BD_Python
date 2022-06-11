import json
from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, flash, json
from pip._vendor import requests

from models.model import Arl
from utils.db import db


arl = Blueprint('python_arl_routes', __name__)


@arl.route('/register_arl', methods=['POST','GET'])
def create():
    if 'admin' in session:
        arl_name = request.form["arl_name"]

        arl = Arl(arl_name)

        db.session.add(arl)
        db.session.commit()
        
        return redirect(url_for('python_admin_routes.info_empleado'))

@arl.route('/show_book')
def show():
    if 'admin' in session:
        movies = Arl.all()
        return render_template('./comment/show.html', movies=movies)



@arl.route('/delete_book/<id>')
def delete():
    if 'admin' in session:
        comment = Arl.query.get(id)

        db.session.delete(comment)
        db.session.commit()



def cont_books():
    return Arl.query.count()
