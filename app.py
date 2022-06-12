from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.user import user
from routes.empleado import empleado
from routes.admin import admin
from routes.dependencia import dependencia
from routes.cargo import cargo
from routes.arl import arl
from routes.pension import pension
from routes.eps import eps
from routes.author import author
from routes.book import book
from routes.publicadores import publicador
from routes.data import data
from connection import connections





app = Flask(__name__)
"""
recordar ls sintaxs para llamar la base de datos 'mysql://username:contrasena@localhost/nombre_BD'

Este nombre de la base de datos a ser local cada uno debe tener una

"""
app.secret_key = 'my_secret_key'



uri = 'mysql://root:root@localhost/proyectobd'

uri = 'mysql://root:Dura2558//@localhost/cine'

uri = connections()



"""
Se configura la bd para que el prog pueda acceder
"""

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#Conexion con SLQAlchemy
SQLAlchemy(app)


"""
con el blue print traemos la informacion que se va hacer en la routes

"example" - es el nombre que se dio en el ruteo 

"""

app.register_blueprint(user)
app.register_blueprint(empleado)
app.register_blueprint(cargo)
app.register_blueprint(admin)
app.register_blueprint(arl)
app.register_blueprint(dependencia)
app.register_blueprint(pension)
app.register_blueprint(eps)
app.register_blueprint(author)
app.register_blueprint(publicador)
app.register_blueprint(book)
