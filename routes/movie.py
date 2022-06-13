import json
from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, flash, json
from pip._vendor import requests

from models.model import Pelicula, Genre
from utils.db import db
import pandas as pd


movie = Blueprint('python_movie_routes', __name__)


@movie.route('/register_movie', methods=['POST','GET'])
def create():
    if 'admin' in session:
        title = request.form["titulol_movie"]
        year = request.form["year_movie"]
        genre_id = Genre.query.filter_by(genre_name = (request.form["genre_id"])).first().id 
        
        crear_pelicula(title, year,genre_id)
        
        return redirect(url_for('python_admin_routes.info_pelicula'))
        

@movie.route('/show_movie')
def show():
    if 'admin' in session:
        movies = Pelicula.all()
        return render_template('./comment/show.html', movies=movies)



@movie.route('/delete_movie/<id>')
def delete():
    if 'admin' in session:
        comment = Pelicula.query.get(id)

        db.session.delete(comment)
        db.session.commit()

def crear_pelicula(title, year,genre_id):
    movie = Pelicula(title, year,genre_id)

    db.session.add(movie)
    db.session.commit()


def cont_movies():
    return Pelicula.query.count()

def get_libros():
    return Pelicula.query.all()


def to_dict(row):
    if row is None:
        return None

    rtn_dict = dict()
    keys = row.__table__.columns.keys()
    for key in keys:
        rtn_dict[key] = getattr(row, key)
    return rtn_dict


@movie.route('/excle_pelicula', methods=['GET', 'POST'])        
def exportar_movie_pdf():
    data = get_libros()
    data_list = [to_dict(item) for item in data]
    df = pd.DataFrame(data_list)
    filename = "C:/Users/juanf/Documents/Universidad/Pr_BD/Proyecto_Final_BD_Python/export_pelicula.xlsx"
    print("Filename: "+filename)   
    
       
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer, sheet_name='Registrados')
    writer.save()
    
    return redirect(url_for('python_admin_routes.info_empleado'))