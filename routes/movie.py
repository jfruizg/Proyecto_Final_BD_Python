import json
from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, flash, json
from pip._vendor import requests

from models.model import User,Pelicula, Admin, Empleado, Cliente, Dependencia, Cargo, Eps,Arl, Pension
from utils.db import db


user = Blueprint('python_movie_routes', __name__)


@user.route('/create_moviee', methods=['POST','GET'])
def create():
    if 'admin' in session:
        title = request.form["title"]
        year = request.form["year"]
        genre_id = request.form["genre_id"]

        movie = Pelicula(title, year,genre_id)

        db.session.add(movie)
        db.session.commit()

@user.route('/show_movie')
def show():
    if 'admin' in session:
        movies = Pelicula.all()
        return render_template('./comment/show.html', movies=movies)



@user.route('/delete_movie/<id>')
def delete():
    if 'admin' in session:
        comment = Pelicula.query.get(id)

        db.session.delete(comment)
        db.session.commit()









