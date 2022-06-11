import json
from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, flash, json
from pip._vendor import requests

from models.model import Autor
from utils.db import db


author = Blueprint('python_author_routes', __name__)


@author.route('/register_author', methods=['POST','GET'])
def create():
    if 'admin' in session:
        author_complete_name = request.form["author_complete_name"]

        autor = Autor(author_complete_name)

        db.session.add(autor)
        db.session.commit()
        
        return redirect(url_for('python_admin_routes.info_libro'))

@author.route('/show_pension')
def show():
    if 'admin' in session:
        movies = Autor.all()
        return render_template('./comment/show.html', movies=movies)



@author.route('/delete_pension/<id>')
def delete():
    if 'admin' in session:
        comment = Autor.query.get(id)

        db.session.delete(comment)
        db.session.commit()

def all_authors():
    return Autor.query.all()

def get_author_id(author_complete_name):
    return Autor.query.filter_by(author_complete_name = author_complete_name).first().id

def cont_books():
    return Autor.query.count()