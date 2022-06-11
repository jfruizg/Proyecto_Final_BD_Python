from enum import unique

from sqlalchemy import true
from utils.db import db
import datetime
class Empleado(db.Model):
    __tablename__ = 'empleados'

    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())
    name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    username = db.Column(db.String(200), unique=true)
    sueldo = db.Column(db.Integer)
    atiende = db.relationship('Atiende')
    empleado_nomina = db.relationship('EmpleadoNomina')
    vacaciones = db.relationship('Vacacion')
    incapacidad = db.relationship('Incapcidad')

    def __init__(self, name, last_name,username, email):
        self.name = name
        self.last_name = last_name
        self.username = username
        self.email = email


class EmpleadoNomina(db.Model):
    __tablename__ = 'nomina_empleados'

    id = db.Column(db.Integer, primary_key=True)
    cod_empleado = db.Column(db.Integer, db.ForeignKey('empleados.id'))
    id_dependencia = db.Column(db.Integer, db.ForeignKey('dependencias.id'))
    id_cargo = db.Column(db.Integer, db.ForeignKey('cargos.id'))
    id_eps = db.Column(db.Integer, db.ForeignKey('eps.id'))
    id_arl = db.Column(db.Integer, db.ForeignKey('arls.id'))
    id_pension = db.Column(db.Integer, db.ForeignKey('pensiones.id'))


class Dependencia(db.Model):
    __tablename__ = 'dependencias'

    id = db.Column(db.Integer, primary_key=True)
    dependencia = db.Column(db.String(256), unique=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())
    empleados = db.relationship('EmpleadoNomina')

    def __init__(self, dependencia):
        self.dependencia = dependencia


class Cargo(db.Model):
    __tablename__ = 'cargos'

    id = db.Column(db.Integer, primary_key=True)
    cargo = db.Column(db.String(256), unique=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())
    empleados = db.relationship('EmpleadoNomina')

    def __init__(self, cargo):
        self.cargo = cargo


class Eps(db.Model):
    __tablename__ = 'eps'

    id = db.Column(db.Integer, primary_key=True)
    eps = db.Column(db.String(256), unique=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())
    empleados = db.relationship('EmpleadoNomina')

    def __init__(self, eps):
        self.eps = eps


class Arl(db.Model):
    __tablename__ = 'arls'

    id = db.Column(db.Integer, primary_key=True)
    arl = db.Column(db.String(256), unique=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())
    empleados = db.relationship('EmpleadoNomina')

    def __init__(self, arl):
        self.arl = arl


class Pension(db.Model):
    __tablename__ = 'pensiones'

    id = db.Column(db.Integer, primary_key=True)
    pension = db.Column(db.String(256), unique=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())
    empleados = db.relationship('EmpleadoNomina')

    def __init__(self, pension):
        self.pension = pension


class Incapcidad(db.Model):
    __tablename__ = 'incapacidad'

    id = db.Column(db.Integer, primary_key=True)
    cod_empleado = db.Column(db.Integer, db.ForeignKey('empleados.id'))
    novedad_incapacidad = db.Column(db.Boolean)
    num_dias = user_tipe = db.Column(db.Integer)
    fecha_inicio = db.Column(db.DateTime, default=datetime.datetime.now())
    fecha_finalizacion = db.Column(db.DateTime)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())
    
    def __init__(self, cod_empleado):
        self.cod_empleado = cod_empleado


class Vacacion(db.Model):
    __tablename__ = 'vacaciones'

    id = db.Column(db.Integer, primary_key=True)
    cod_empleado = db.Column(db.Integer, db.ForeignKey('empleados.id'))
    novedad_vacaciones = db.Column(db.Boolean)
    num_dias = user_tipe = db.Column(db.Integer)
    fecha_inicio = db.Column(db.DateTime, default=datetime.datetime.now())
    fecha_finalizacion = db.Column(db.DateTime)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())


class Novedad(db.Model):
    __tablename__ = 'novedades'

    id = db.Column(db.Integer, primary_key=True)
    num_dias_trabajados = db.Column(db.Integer)
    cod_incapacidad = db.Column(db.Integer, db.ForeignKey('incapacidad.id'))
    cod_vacaciones = db.Column(db.Integer, db.ForeignKey('vacaciones.id'))
    bonificacion = db.Column(db.Integer)
    transporte = db.Column(db.Integer)


class Cliente(db.Model):
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    correo = db.Column(db.String(256))
    direccion = db.Column(db.String(256))
    username = db.Column(db.String(200), unique=true)
    telefono = db.Column(db.Integer)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())
    atiende = db.relationship('Atiende')

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

    def __init__(self, id_cliente, id_empleado, fecha_atencion):
        self.id_cliente = id_cliente
        self.id_empleado = id_empleado
        self.fecha_atencion = fecha_atencion
        
class Genre(db.Model):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String(250))
    pelicula = db.relationship("Pelicula")
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())
     
class Pelicula(db.Model):
    __tablename__ = 'peliculas'
     
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    year = db.Column(db.Integer)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())
    
class Autor(db.Model): 
    __tablename__ = 'autores'
    
    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())
    pelicula = db.relationship("Libro")
    
    
    

class Publicador(db.Model):  
    __tablename__ = 'publicadores' 
    
    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String(200))
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())   
    pelicula = db.relationship("Libro")
    
class Libro(db.Model):
    __tablename__ = 'libros' 
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    avrege_raiting = db.Column(db.String(100))
    isbn = db.Column(db.String(100), unique=True)
    isbn13 = db.Column(db.String(100), unique=True)
    language_code = db.Column(db.String(100))
    num_pages = db.Column(db.Integer)
    raiting_count = db.Column(db.Integer)
    text_reviews = db.Column(db.String(100))
    text_reviews_count = db.Column(db.Integer)
    publication_date = db.Column(db.DateTime, default=datetime.datetime.now())
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())
    publisher_id = db.Column(db.Integer, db.ForeignKey('publicadores.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('autores.id'))
    venta = db.relationship('Venta')
    
class Venta(db.Model):
    __tablename__ = 'ventas'

    id = db.Column(db.Integer, primary_key=True)
    libro_id = db.Column(db.Integer, db.ForeignKey('libros.id'))
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleados.id'))


class Renta(db.Model):
    __tablename__ = 'rentas'

    id = db.Column(db.Integer, primary_key=True)
    pelicula_id = db.Column(db.Integer, db.ForeignKey('peliculas.id'))
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleados.id'))



class Admin(db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=true)
    name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, username,name,last_name,email):
        self.username = username
        self.name = name
        self.last_name = last_name
        self.email = email
    
    
        
       
    
    

    
     
