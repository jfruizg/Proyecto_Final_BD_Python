#blueprint es una forma de conectar los archivos a l;a base de datos
from flask import Blueprint

example = Blueprint('example', __name__)

#En este espacio se agrega los metodos que va generar la pagina web

@example.route("/")
def home():
    return "hello world example"