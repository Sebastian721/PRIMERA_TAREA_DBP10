from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sebastian2103@localhost:5432/ejercicio3db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.create_all()
migrate=Migrate()

migrate.init_app(app,db)



class usuario(db.Model):
    __tablename__ = 'usuarios'
    _id = db.Column(db.String(75), primary_key=True)
    nombre = db.Column(db.String(75))
    apellido = db.Column(db.String(75))
    password = db.Column(db.String(75))
    def __init__(self, _id, nombre, apellido, password):
        self._id = _id
        self.nombre = nombre
        self.apellido = apellido
        self.password = password

class transporte(db.Model):
    __tablename__ = 'transportes'
    _id = db.Column(db.String(75), primary_key=True)
    tipo = db.Column(db.String(75))

    def __init__(self, _id, tipo):
        self._id = _id
        self.tipo = tipo

class orden(db.Model):
    __tablename__ = 'ordenes'
    _id = db.Column(db.String(75), primary_key=True)
    tamano = db.Column(db.String(75))
    precio = db.Column(db.String(75))

    def __init__(self, _id, tamano, precio):
        self._id = _id
        self.tamano = tamano
        self.precio = precio

usuarios=usuario(1,'Martin','Jimenez','1234')
usuarios=usuario(2,'Julian','Bazola','password')
usuarios3=usuario(3,'Alberto','Castro','contra')
usuarios4=usuario(4,'Alfonso','Villanueva','sena')
usuarios5=usuario(5,'Javier','Mendoza','4321')

transporte1=transporte(1, 'bicicleta')
transporte2=transporte(2, 'camion')
transporte3=transporte(3, 'camion')
transporte4=transporte(4, 'bicicleta')
transporte5=transporte(5, 'camion')

orden1=orden(1,3,100)
orden2=orden(2,1,10)
orden3=orden(3,5,200)
orden4=orden(4,6,170)
orden5=orden(5,2,300)


@app.route('/')
def index():
    db.session.add(orden1)
    db.session.commit()
    db.session.add(orden2)
    db.session.commit()
    db.session.add(orden3)
    db.session.commit()
    db.session.add(orden4)
    db.session.commit()
    db.session.add(orden5)
    db.session.commit()

    lista=orden.query.all()
    lista = [
            {
                 "precio": orden.precio,
            } for orden in lista]
    
    html=''
    for e in lista:
        html=html+'<h1>'
        html=html+e['precio']
        html=html+'</h1>'
    return html
