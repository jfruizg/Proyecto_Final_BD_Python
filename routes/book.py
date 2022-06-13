import json
from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, flash, json
from pip._vendor import requests

from models.model import Libro, Pelicula, Libro
from routes.author import get_author_id
from routes.publicadores import get_publicadores_id
from utils.db import db

book = Blueprint('python_book_routes', __name__)


@book.route('/register_book', methods=['POST', 'GET'])
def create():
    if 'admin' in session:
        title = request.form["titulo"]
        avrege_raiting = request.form["avrege_raiting"]
        isbn = request.form["isbn"]
        isbn13 = request.form["isbn13"]
        language_code = request.form["language_code"]
        raiting_count = request.form["raiting_count"]
        text_reviews = request.form["text_reviews"]
        num_pages = request.form["num_pages"]
        text_reviews_count = request.form["text_reviews_count"]
        autor = request.form["author_id"]
        publicador = request.form["publicador_id"]

        id_autor = get_author_id(autor)
        id_publicador = get_publicadores_id(publicador)

        book = Libro(title, avrege_raiting, isbn, isbn13, language_code, num_pages, raiting_count, text_reviews,
                     text_reviews_count, id_publicador, id_autor)

        db.session.add(book)
        db.session.commit()

        return redirect(url_for('python_admin_routes.info_libro'))


@book.route('/delete_book/<id>')
def delete_book(id):
    if 'admin' in session:
        comment = Libro.query.get(id)

        db.session.delete(comment)
        db.session.commit()
        return redirect(url_for('python_admin_routes.info_libro'))


def cont_books():
    return Libro.query.count()
