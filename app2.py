from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import make_response, jsonify


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sebastian2103@localhost:5432/ejercicio2db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:sebastian2103@localhost:3306/ejercicio2db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate=Migrate()
db.create_all()

migrate.init_app(app,db)

class profesor(db.Model):
    __tablename__ = 'profesores'
    _id = db.Column(db.String(75), primary_key=True)
    nombre = db.Column(db.String(75))
    apellido = db.Column(db.String(75))
    sueldo = db.Column(db.String(75))
    especialidad = db.Column(db.String(75))

    def __init__(self, _id, nombre, apellido, sueldo, especialidad):
        self._id = _id
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo
        self.especialidad = especialidad

class estudiante(db.Model):
    __tablename__ = 'estudiantes'
    _id = db.Column(db.String(75), primary_key=True)
    nombre = db.Column(db.String(75))
    apellido = db.Column(db.String(75))
    seccion = db.Column(db.String(75))

    def __init__(self, _id, nombre, apellido, seccion):
        self._id = _id
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion

class Curso(db.Model):
    __tablename__ = 'cursos'
    _id = db.Column(db.String(75), primary_key=True)
    tutor = db.Column(db.String(75))
    area = db.Column(db.String(75))
    creditos = db.Column(db.String(75))
    aula = db.Column(db.String(75))

    def __init__(self, _id, tutor, area,creditos,aula):
        self._id = _id
        self.tutor = tutor
        self.area = area
        self.creditos = creditos
        self.aula = aula

class seccion(db.Model):
    __tablename__ = 'secciones'
    _id = db.Column(db.String(75), primary_key=True)
    aula = db.Column(db.String(75))
    tutor = db.Column(db.String(75))
    piso = db.Column(db.String(75))
    grado = db.Column(db.String(75))

    def __init__(self, _id, aula, tutor, piso, grado):
        self._id = _id
        self.aula = aula
        self.tutor = tutor
        self.piso = piso
        self.grado = grado



#estudiantes=estudiante(11,'Roberto','Jimenez','1A')
#estudiantes2=estudiante(2,'Matias','Gallardo','1B')
#estudiantes3=estudiante(3,'Lucia','Hernandez','2A')
#estudiantes4=estudiante(4,'Veronica','Aguilar','2B')
#estudiantes5=estudiante(5,'Julia','Gomez','3A')
#estudiantes6=estudiante(6,'Julio','Suarez','3B')
#estudiantes7=estudiante(7,'Maria','Castro','3C')
#estudiantes8=estudiante(8,'Mariano','Guazman','4A')
#estudiantes9=estudiante(9,'Roberto','Allcca','4B')
#estudiantes10=estudiante(10,'Gonzalo','Menendez','5A')

#cursos1 = Curso(11, "Andrea", "matematica", 3, "1A")
#cursos2 = Curso(12, "Julio", "historia", 3, "1A")
#cursos3 = Curso(13, "Gerardo", "comunicacion", 4, "1B")
#cursos4 = Curso(14, "Marcia", "matematica", 4, "1C")
#cursos5 = Curso(15, "Jorge", "ingles", 3, "1B")
#cursos6 = Curso(16, "Iris", "ciencia", 3, "2A")
#cursos7 = Curso(17, "Pamela", "computacion", 2, "3A")
#cursos8 = Curso(18, "Gilberto", "comunicacion", 4, "1A")
#cursos9 = Curso(19, "Sandra", "arte", 2, "3B")
#cursos10 = Curso(20, "Elisa", "educacion fisica", 1, "2A")

secciones1 = seccion(11, "1.01", "Andrea", 1, "1A")
secciones2 = seccion(2, "1.02", "Jorge", 1, "1C")
secciones3 = seccion(3, "1.01", "Guillermo", 1, "1B")
secciones4 = seccion(4, "1.01", "Massiel", 1, "2C")
secciones5 = seccion(5, "1.01", "Julio", 2, "2B")
secciones6 = seccion(6, "1.01", "Iris", 2, "2A")
secciones7 = seccion(7, "1.01", "Pamela", 2, "3A")
secciones8 = seccion(8, "1.01", "Marcia", 3, "3B")
secciones9 = seccion(9, "1.01", "Sandra", 3, "4A")
secciones10 = seccion(10, "1.01", "Elisa", 3, "5A")



@app.route('/profe')
def profesor():
    docentes=profesor.query.all()
    docentes = [
            {
                 "nombre": profesor.nombre,
                 "apellido":profesor.apellido,
                 "sueldo": profesor.sueldo
            } for profesor in docentes]
    
    html=''
    for e in docentes:
        html=html+'<h1>'
        html=html+e['nombre']
        html=html+' '
        html=html+e['apellido']
        html=html+' '
        html=html+e['sueldo']
        html=html+'</h1>'

    return html



@app.route('/')
def index():
    db.session.add(secciones1)
    db.session.commit()
    db.session.add(secciones2)
    db.session.commit()
    db.session.add(secciones3)
    db.session.commit()
    db.session.add(secciones4)
    db.session.commit()
    db.session.add(secciones5)
    db.session.commit()
    db.session.add(secciones6)
    db.session.commit()
    db.session.add(secciones7)
    db.session.commit()
    db.session.add(secciones8)
    db.session.commit()
    db.session.add(secciones9)
    db.session.commit()
    db.session.add(secciones10)
    db.session.commit()
    sec=seccion.query.all()
    sec = [
            {
                 "tutor": seccion.tutor,
                 "piso":seccion.piso,
                 "grado": seccion.grado,
                 "aula": seccion.aula
            } for seccion in sec] 
    html=''
    for e in sec:
        html=html+'<h1>'
        html=html+e['tutor']
        html=html+' '
        html=html+e['piso']
        html=html+' '
        html=html+e['aula']
        html=html+' '
        html=html+e['grado']
        html=html+'</h1>'
    return html

