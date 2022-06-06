from utils.db import db
import datetime

class Dependencia(db.Model):
    __tablename__ = 'dependencias'

    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())
    empleados = db.relationship('Empleado')

    def __init__(self, dependencia):
        self.dependencia = dependencia