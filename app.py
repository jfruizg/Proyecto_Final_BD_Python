from flask import Flask
from flask_recaptcha import ReCaptcha
from flask_sqlalchemy import SQLAlchemy
from routes.example import example


app = Flask(__name__)
"""
recordar ls sintaxs para llamar la base de datos 'mysql://username:contrasena@localhost/nombre_BD'

Este nombre de la base de datos a ser local cada uno debe tener una

"""

uri = 'mysql://root:felipe1972@localhost/proyecto_final_bd'

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

app.config.update(dict(
    RECAPTCHA_ENABLED = True,
    RECAPTCHA_SITE_KEY = "6LeKOaMZAAAAAI7L6TVsZa9A2t6-9LDVYSVqX9ZP",
    RECAPTCHA_SECRET_KEY = "6LeKOaMZAAAAAKw9nhAjnpzrzrC3R0YYRf-kKDH1",
))

recaptcha = ReCaptcha()
recaptcha.init_app(app)

app.register_blueprint(example)
