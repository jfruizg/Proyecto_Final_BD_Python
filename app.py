from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.user import user
from routes.empleado import empleado
from connection import connections





app = Flask(__name__)
"""
recordar ls sintaxs para llamar la base de datos 'mysql://username:contrasena@localhost/nombre_BD'

Este nombre de la base de datos a ser local cada uno debe tener una

"""
app.secret_key = 'my_secret_key'



uri = 'mysql://root:estefa03@localhost/Proyecto_Final'

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