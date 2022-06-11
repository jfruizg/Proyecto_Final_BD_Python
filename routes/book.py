import json
from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, flash, json
from pip._vendor import requests

from models.model import Libro, Pelicula
from utils.db import db


book = Blueprint('python_book_routes', __name__)


@book.route('/create_book', methods=['POST','GET'])
def create():
    if 'admin' in session:
        title = request.form["title"]
        year = request.form["year"]
        genre_id = request.form["genre_id"]

        movie = Pelicula(title, year,genre_id)

        db.session.add(movie)
        db.session.commit()

@book.route('/show_book')
def show():
    if 'admin' in session:
        movies = Pelicula.all()
        return render_template('./comment/show.html', movies=movies)



@book.route('/delete_book/<id>')
def delete():
    if 'admin' in session:
        comment = Pelicula.query.get(id)

        db.session.delete(comment)
        db.session.commit()



def cont_books():
    return Libro.query.count()
