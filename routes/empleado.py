import json
from MySQLdb import IntegrityError
from flask import Blueprint, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from routes.pension import create_pension, get_pension_id
from utils.db import db
from models.model import Empleado, EmpleadoNomina, Pelicula
from routes.arl import get_arl, get_arl_id, create_arl
from routes.cargo import get_cargo, get_cargo_id, create_cargo
from routes.dependencia import get_dependencia, get_dependencia_id, create_dependencia
from routes.eps import eps, get_eps_id, create_eps
from routes.genre import crear_genero, get_genre_id
from routes.movie import crear_pelicula
from routes.author import create_author, get_author_id
from routes.publicadores import create_publicador, get_publicadores_id
from routes.book import create_libros
import pandas as pd
import pdfkit as pdfkit


empleado = Blueprint('python_empleado_routes', __name__)


@empleado.route("/new_employee", methods=['POST', 'GET'])
def create_emp():
    name = request.form['name']
    last_name = request.form['last_name']
    username = request.form['username']
    email = request.form['email']
    new_emp = Empleado(name, last_name, username, email)
    db.session.add(new_emp)
    db.session.commit()

    return redirect("/")


@empleado.route("/register_nomina", methods=['POST', 'GET'])
def create_empleado_nomina():
    empleado_id = get_empleado_id(request.form['empleado_id'])
    arl_id = get_arl_id(request.form['arl_id'])
    cargo_id = get_cargo_id(request.form['cargo_id'])
    eps_id = get_eps_id(request.form['eps_id']) 
    dependencia_id = get_dependencia_id(request.form['dependencia_id'])
    pension_id = get_pension_id(request.form['pension_id'])
    
  
    new_emp_nomina = EmpleadoNomina(empleado_id, dependencia_id, cargo_id, eps_id, arl_id, pension_id)
    db.session.add(new_emp_nomina)
    db.session.commit()

    return redirect(url_for('python_admin_routes.info_empleado'))

@empleado.route("/delete_emp/<id>")
def delete_emp(id):
    empleado = Empleado.query.get(id)
    db.session.delete(empleado)
    db.session.commit()
    return redirect(url_for('python_admin_routes.info_empleado'))


@empleado.route("/update_emp/<id>", methods=['POST', 'GET'])
def update_emp(id):
    empleado = Empleado.query.get(id)
    if request.method == 'POST':

        empleado.id = request.form['id']
        empleado.user_id = request.form['user_id']
        db.session.commit()
        return redirect(url_for('empleado.ingreso'))

    else:

        return render_template('index.html', empleado=empleado)


@empleado.route("/show_emp")
def show_emp():
    empleado = Empleado.all()
    return render_template('./comment/show.html', empleado=empleado)


def cont_empleados():
    return Empleado.query.count()


def get_empleados():
    return Empleado.query.all()

def get_empleado_id(empleado):
    return Empleado.query.filter_by(username = empleado).first().id

def get_empleado_code(empleado):
    return Empleado.query.filter_by(codigo = empleado).first().id


@empleado.route("/show_data")
def show_data():
    return render_template('./views/datos.html')

@empleado.route('/data', methods=['POST', 'GET'])
def data():
    if request.method == 'POST':
        file = request.form["upload_excel_file"]
        data = pd.read_excel(file)

     
        valores = data.values    
        crear_datos_empleado(valores)
        create_empleados_data(valores)
        create_empleado_nomina(valores)
        
        print("Paso")
        
        return redirect(url_for('python_admin_routes.info_empleado'))


    return render_template("./views/Admin/datos.html")

@empleado.route('/data_dt', methods=['POST', 'GET'])
def data_dt():
    file_name = request.form["upload_dat_file"]
    file = open(file_name, encoding="utf8")
    create_gener_dat(file)
    crear_pelicula(file)
    print("Listo")
    return redirect(url_for('python_admin_routes.info_empleado'))    
    
@empleado.route('/data_json', methods=['POST', 'GET'])    
def data_json():
    create_authors()
    create_libro()
    print("Se acabo")
    
    return redirect(url_for('python_admin_routes.info_empleado'))  

def create_data(cargo,eps,arl,dependencia,pension):
    create_cargo(cargo)
    create_eps(eps)
    create_arl(arl)
    create_dependencia(dependencia)
    create_pension(pension)
    
   
def create_empleado(nombre_completo,username_empleado,correo,codigo):
    empleado = Empleado(nombre_completo,username_empleado,correo,codigo)
            
    db.session.add(empleado)
    db.session.commit() 
  
def data_crear_cargo(variable):
    for i in variable:
        create_cargo(i)
        
def data_crear_eps(variable):
    for i in variable:
        create_eps(i)

def data_crear_arl(variable):
    for i in variable:
        create_arl(i)        
        
def data_crear_dependencia(variable):
    for i in variable:
        create_dependencia(i) 
      
def data_crear_pension(variable):
    for i in variable:
        create_pension(i)                  
    
def crear_datos_empleado(valores):
    dependencia = []
    cargo = []
    eps = []
    arl = []
    pension = []
    for row in valores:
        dependencia.append(row[2])
        cargo.append(row[3])
        eps.append(row[5])
        arl.append(row[6])
        pension.append(row[7])
    
    
    data_crear_cargo(list(set(cargo)))
    data_crear_arl(list(set(arl)))
    data_crear_dependencia(list(set(dependencia)))
    data_crear_eps(list(set(eps)))
    data_crear_pension(list(set(pension))) 
       
       
def create_empleados_data(valores):
    cont = 0
    for row in valores:
        cont = cont + 1
        codigo = row[0]
        nombre = row[1]
        username = f"empleado {codigo}"
        correo = f"empleado {codigo}@gmail.com"     
        create_empleado(nombre,username,correo,codigo)  
       
def create_empleado_nomina(valores):
    for row in valores:
        empleado_id = get_empleado_code(row[0])
        dependencia_id = get_dependencia_id(row[2])
        cargo_id = get_cargo_id(row[3])
        eps_id =  get_eps_id(row[5])
        arl_id = get_arl_id(row[6])
        pension_id = get_pension_id(row[7])
       
        new_emp_nomina = EmpleadoNomina(empleado_id, dependencia_id, cargo_id, eps_id, arl_id, pension_id)
        db.session.add(new_emp_nomina)
        db.session.commit()
        
def create_gener_dat(file):
    genre = []
    for linea in file:
        linea = linea.split("::")
        genre.append(linea[2])
    
    genre_list = list(set(genre)) 
        
    for i in genre_list:
        crear_genero(i)
        
      
def crear_pelicula_dat(file):
    for linea in file:
        titulo = linea[1]
        titulo_rep = titulo.split(" ")
        anio = titulo_rep.pop()
        gener_id = get_genre_id(linea[2])
        crear_pelicula(titulo, anio,gener_id)
       
        

def to_dict(row):
    if row is None:
        return None

    rtn_dict = dict()
    keys = row.__table__.columns.keys()
    for key in keys:
        rtn_dict[key] = getattr(row, key)
    return rtn_dict 
    
@empleado.route('/excel_empleado', methods=['GET', 'POST'])        
def exportar_empleado_excel():
    data = get_empleados()
    data_list = [to_dict(item) for item in data]
    df = pd.DataFrame(data_list)
    filename = "C:/Users/juanf/Documents/Universidad/Pr_BD/Proyecto_Final_BD_Python/export_empleados.xlsx"
    print("Filename: "+filename)   
    
       
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer, sheet_name='Registrados')
    writer.save()
    
    return redirect(url_for('python_admin_routes.info_empleado')) 



def data_crear_author(variable):
    for i in variable:
        create_author(i) 
        
def data_crear_publidor(variable):
    for i in variable:
        create_publicador(i)   
        
def create_libro():
    file_name = request.form["upload_dat_file"]
    autor = []
    publicador = []
    with open("books.json", encoding="utf8") as file:
        data = json.load(file)
        for client in data:
            title = (client['title'])
            autor = (client['authors'])
            average_rating = (client['average_rating'])
            isbn = (client['isbn'])
            isbn13 = (client['isbn13'])
            language_code = (client['language_code'])
            num_pages = (client['num_pages'])
            ratings_count = (client['ratings_count'])
            text_reviews_count = (client['text_reviews_count'])
            isbn = (client['isbn'])
            publication_date = (client['publication_date'])
            publicador = (client['publisher'])
            
            create_libros(title, average_rating, isbn, isbn13, language_code, num_pages, ratings_count, "text_reviews",
                     text_reviews_count, get_publicadores_id(publicador), get_author_id(autor))
            

def create_authors():
    file_name = request.form["upload_dat_file"]
    autor = []
    publicador = []
    with open("books.json", encoding="utf8") as file:
        data = json.load(file)
        for client in data:
            autor.append(client['authors'])
            publicador.append(client['publisher'])
    
    autor_name = list(set(autor)) 
    print(autor_name)  
    publicador_name = list(set(publicador)) 
    print(publicador_name) 
    data_crear_author(autor_name)
    data_crear_publidor(publicador_name)
    
    
    