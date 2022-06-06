from utils.db import db
import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(248))
    last_name = db.Column(db.String(100))
    user_tipe = db.Column(db.Integer)
    username = db.Column(db.String(50), unique=True)
    empleados = db.relationship('Empleado')
    clientes = db.relationship('Cliente')
    admin = db.relationship('Admin')

    def __init__(self, username, password, email):
        self.username = username
        self.password = self.__create_password(password)
        self.email = email

    def __create_password(self, password):
        return generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

class Empleado(db.Model):
    __tablename__ = 'empleados'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, user_id, id):
        self.user_id = user_id
        self.id = id


class Cliente(db.Model):
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, user_id, id):
        self.user_id = user_id
        self.id = id


class Admin(db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, user_id, id):
        self.user_id = user_id
        self.id = id
