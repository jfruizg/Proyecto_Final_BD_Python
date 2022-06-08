import json
from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, flash, json
from pip._vendor import requests

from models.model import User,Pelicula, Genre,Admin, Empleado, Cliente, Dependencia, Cargo, Eps,Arl, Pension
from utils.db import db

genre = Blueprint('python_genre_routes', __name__)

@genre.route('/create_moviee', methods=['POST','GET'])
def create():
    if 'admin' in session:
        genre = request.form["genre"]
        atiende = request.form["atiende"]


        genre = Pelicula(genre, atiende)

        db.session.add(genre)
        db.session.commit()

@genre.route('/show_movie')
def show():
    if 'admin' in session:
        movies = Genre.all()
        return render_template('./comment/show.html', movies=movies)



@genre.route('/delete_movie/<id>')
def delete():
    if 'admin' in session:
        comment = Pelicula.query.get(id)

        db.session.delete(comment)
        db.session.commit()