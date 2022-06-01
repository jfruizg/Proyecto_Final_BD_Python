from app import app
from utils.db import db

#aca generamos la BD
with app.app_context():
  db.create_all()

#Con este metodo corremos el programa en local - python indedx.py - es el codigo que se usa para correr
if __name__ == "__main__":
  app.run(debug=True)