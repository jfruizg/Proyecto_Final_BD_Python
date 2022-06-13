import json
from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, flash, json
from pip._vendor import requests

from models.model import Pelicula, Genre, Empleado, Cliente, Dependencia, Cargo, Eps,Arl, Pension
from utils.db import db

genre = Blueprint('python_genre_routes', __name__)

@genre.route('/register_genre', methods=['POST','GET'])
def create():
    if 'admin' in session:
        genre = request.form["genre_complete_name"]
        
        genre = Genre(genre)

        db.session.add(genre)
        db.session.commit()
        
        return render_template('./views/Admin/peliculadmin.html')

@genre.route('/show_movie')
def show():
    if 'admin' in session:
        movies = Genre.all()
        return render_template('./comment/show.html', movies=movies)

def all_genre():
    return Genre.query.all()

@genre.route('/delete_movie/<id>')
def delete():
    if 'admin' in session:
        comment = Genre.query.get(id)

        db.session.delete(comment)
        db.session.commit()



