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
    id_dependencia = db.Column(db.Integer, db.ForeignKey('dependencias.id'))
    id_cargo = db.Column(db.Integer, db.ForeignKey('cargos.id'))
    id_eps = db.Column(db.Integer, db.ForeignKey('eps.id'))
    id_arl = db.Column(db.Integer, db.ForeignKey('arls.id'))
    id_pension = db.Column(db.Integer, db.ForeignKey('pensiones.id'))
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())
    incapacidad = db.relationship('Incapacidad')
    atiende = db.relationship('Atiende')
    renta = db.relationship('Renta')
    venta = db.relationship('Venta')

    def __init__(self, user_id, id):
        self.user_id = user_id
        self.id = id

class Dependencia(db.Model):
    __tablename__ = 'dependencias'

    id = db.Column(db.Integer, primary_key=True)
    dependencia = db.Column(db.String(256), unique=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())
    empleados = db.relationship('Empleado')

    def __init__(self, dependencia):
        self.dependencia = dependencia

class Cargo(db.Model):
    __tablename__ = 'cargos'

    id = db.Column(db.Integer, primary_key=True)
    cargo = db.Column(db.String(256), unique=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())
    empleados = db.relationship('Empleado')

    def __init__(self, cargo):
        self.cargo = cargo

class Eps(db.Model):
    __tablename__ = 'eps'

    id = db.Column(db.Integer, primary_key=True)
    eps = db.Column(db.String(256), unique=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())
    empleados = db.relationship('Empleado')

    def __init__(self, eps):
        self.eps = eps

class Arl(db.Model):
    __tablename__ = 'arls'

    id = db.Column(db.Integer, primary_key=True)
    arl = db.Column(db.String(256), unique=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())
    empleados = db.relationship('Empleado')

    def __init__(self, arl):
        self.arl = arl

class Pension(db.Model):
    __tablename__ = 'pensiones'

    id = db.Column(db.Integer, primary_key=True)
    pension = db.Column(db.String(256), unique=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())
    empleados = db.relationship('Empleado')

    def __init__(self, pension):
        self.pension = pension

class Incapacidad(db.Model):
    __tablename__ = 'incapacidad'

    id = db.Column(db.Integer, primary_key=True)
    cod_empleado = db.Column(db.Integer, db.ForeignKey('empleados.id'))
    id_novedad = db.Column(db.Integer, db.ForeignKey('tiponovedad.id'))
    num_dias = user_tipe = db.Column(db.Integer)
    fecha_inicio = db.Column(db.DateTime, default=datetime.datetime.now())
    fecha_finalizacion = db.Column(db.DateTime)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())
    tipo_incapacidad = db.relationship('TipoNovedad')

    def __init__(self, cod_empleado,id_novedad, num_dias,fecha_inicio , fecha_finalizacion):
        self.cod_empleado = cod_empleado
        self.id_novedad = id_novedad
        self.num_dias = num_dias
        self.fecha_inicio = fecha_inicio
        self.fecha_finalizacion = fecha_finalizacion



class TipoNovedad(db.Model):
    __tablename__ = 'tiponovedad'

    id = db.Column(db.Integer, primary_key=True)
    incapacidad = db.Column(db.String(256), unique=True)

    def __init__(self, incapacidad):
        self.incapacidad = incapacidad


class Cliente(db.Model):
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())
    atiende = db.relationship('Atiende')
    renta = db.relationship('Renta')
    venta = db.relationship('Venta')

    def __init__(self, user_id, id):
        self.user_id = user_id
        self.id = id

class Atiende(db.Model):
    __tablename__ = 'atiende'

    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    id_ermpleado = db.Column(db.Integer, db.ForeignKey('empleados.id'))
    fecha_atencion = db.Column(db.DateTime, default=datetime.datetime.now())
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, id_cliente, id_empleado,fecha_atencion):
        self.id_cliente = id_cliente
        self.id_empleado = id_empleado
        self.fecha_atencion = fecha_atencion

class Libro(db.Model):
    __tablename__ = 'libros'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    avrege_raiting = db.Column(db.String(100))
    isbn = db.Column(db.String(100))
    isbn13 = db.Column(db.String(100))
    language_code = db.Column(db.String(100))
    num_pages = db.Column(db.Integer)
    raiting_count = db.Column(db.Integer)
    text_reviews = db.Column(db.String(100))
    text_reviews_count = db.Column(db.Integer)
    publication_date = db.Column(db.DateTime, default=datetime.datetime.now())
    publisher = db.Column(db.String(100))
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())
    venta = db.relationship('Venta')

class Pelicula(db.Model):
    __tablename__ = 'peliculas'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    year = db.Column(db.Integer)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    renta = db.relationship('Renta')

class Genre(db.Model):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(100))
    atiende = db.relationship('Pelicula')

class Venta(db.Model):
    __tablename__ = 'ventas'

    id = db.Column(db.Integer, primary_key=True)
    libro_id = db.Column(db.Integer, db.ForeignKey('libros.id'))
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleados.id'))
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))


class Renta(db.Model):
    __tablename__ = 'rentas'

    id = db.Column(db.Integer, primary_key=True)
    pelicula_id = db.Column(db.Integer, db.ForeignKey('peliculas.id'))
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleados.id'))
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))

class Admin(db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, user_id, id):
        self.user_id = user_id
        self.id = id
