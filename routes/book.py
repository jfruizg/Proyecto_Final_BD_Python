import json
from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, flash, json
from pip._vendor import requests

from models.model import User,Pelicula, Libro,Admin, Empleado, Cliente, Dependencia, Cargo, Eps,Arl, Pension
from utils.db import db


book = Blueprint('python_book_routes', __name__)


@book.route('/create_book', methods=['POST','GET'])
def create():
    if 'admin' in session:
        title = request.form["title"]
        avrege_raiting = request.form["avrege_raiting"]
        author = request.form["author"]
        isbn = request.form["isbn"]
        isbn13 = request.form["isbn13"]
        language_code = request.form["language_code"]
        num_pages= request.form["num_pages"]
        raiting_count = request.form["raiting_count"]
        text_reviews = request.form["text_reviews"]
        text_reviews_count = request.form["text_reviews_count"]
        publication_date = request.form["text_reviews_count"]
        publisher = request.form["publisher"]

        book = Libro(title, author,avrege_raiting, isbn, isbn13, language_code,num_pages,raiting_count, text_reviews,text_reviews_count, publication_date, publisher)

        db.session.add(book)
        db.session.commit()

@book.route('/show_book')
def show():
    if 'admin' in session:
        books = Libro.all()
        return render_template('./comment/show.html', books=books)



@book.route('/delete_book/<id>')
def delete():
    if 'admin' in session:
        comment = Libro.query.get(id)

        db.session.delete(comment)
        db.session.commit()