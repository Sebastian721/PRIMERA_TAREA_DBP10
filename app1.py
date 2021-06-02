import psycopg2 # Importamos la libreria



class Profesor:
    _id = 0
    nombre = ""
    apellido = ""
    email = ""
    curso = ""

    def __init__(self, _id, nombre, apellido,email,curso):
        self._id = _id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.curso = curso

    def getId(self):
        return self._id

class Estudiante:
    _id = 0
    nombre = ""
    apellido = ""
    email = ""
    seccion = ""
    def __init__(self, _id, nombre, apellido,email,seccion):
        self._id = _id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.seccion = seccion

    def getId(self):
        return self._id

class Curso:
    _id = 0
    tutor = ""
    area = ""
    creditos = ""
    aula = ""

    def __init__(self, _id, tutor, area,creditos,aula):
        self._id = _id
        self.tutor = tutor
        self.area = area
        self.creditos = creditos
        self.aula = aula

    def getId(self):
        return self._id

class Sección:
    _id = 0
    aula = ""
    tutor = ""
    piso = ""
    grado = ""

    def __init__(self, _id, aula, tutor, piso, grado):
        self._id = _id
        self.aula = aula
        self.tutor = tutor
        self.piso = piso
        self.grado = grado

    def getId(self):
        return self._id



try:
    credentials = {
        "dbname": "ejercicio1db",
        "user": "postgres",
        "password": "sebasian2103",
        "host": "localhost",
        "port": 5432 
    }
    connect = psycopg2.connect(**credentials) 
except psycopg2.Error as e:
    print("ERROR", e)

cursor = connect.cursor() 



table_name = 'profesor'
cursor.execute("DROP TABLE IF EXISTS %s " % table_name )

cursor.execute("create table %s ( id int, nombre varchar(20), apellido varchar(20), email varchar(30), curso varchar(20) );" % table_name)


p1 = Profesor(1, "Andrea","Galarza","andrea@gmail.com", "matematica")
p2 = Profesor(2, "Julio","Castro","julio@gmail.com", "historia")
p3 = Profesor(3, "Gerardo","Arruela","g123@gmail.com", "comunicacion")
p4 = Profesor(4, "Marcia","Cordova","marca@gmail.com", "matematica")
p5 = Profesor(5, "Jorge","Gonzales","jorgeg@gmail.com", "ingles")
p6 = Profesor(6, "Iris","Quispe","iris_q@gmail.com", "ciencia")
p7 = Profesor(7, "Pamela","Hernandez","pame_h@gmail.com", "computacion")
p8 = Profesor(8, "Gilberto","Huerta","gilbert@gmail.com", "comunicacion")
p9 = Profesor(9, "Sandra","Flores","sanflo@gmail.com", "arte")
p10 = Profesor(10, "Elisa","Galarza","eli@gmail.com", "educacion fisica")

cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [p1._id, p1.nombre, p1.apellido, p1.email, p1.curso])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [p2._id, p2.nombre, p2.apellido, p2.email, p2.curso])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [p3._id, p3.nombre, p3.apellido, p3.email, p3.curso])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [p4._id, p4.nombre, p4.apellido, p4.email, p4.curso])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [p5._id, p5.nombre, p5.apellido, p5.email, p5.curso])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [p6._id, p6.nombre, p6.apellido, p6.email, p6.curso])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [p7._id, p7.nombre, p7.apellido, p7.email, p7.curso])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [p8._id, p8.nombre, p8.apellido, p8.email, p8.curso])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [p9._id, p9.nombre, p9.apellido, p9.email, p9.curso])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [p10._id, p10.nombre, p10.apellido, p10.email, p10.curso])

cursor.execute("SELECT * FROM %s" % table_name)
profesores = cursor.fetchall()

print(" PROFESORES ")
for row in profesores:
    print(row)

table_name = 'estudiante'
cursor.execute("DROP TABLE IF EXISTS %s " % table_name )

cursor.execute("create table %s ( id int, nombre varchar(20), apellido varchar(20), email varchar(30), seccion varchar(20) );" % table_name)


e1 = Estudiante(1, "Josefa", "Martinez", "jmart@gmail.com", "1A")
e2 = Estudiante(1, "Jorge", "Gonzales", "jhong@gmail.com", "1C")
e3 = Estudiante(1, "Luis", "Gamarra", "luisg@gmail.com", "1B")
e4 = Estudiante(1, "Martin", "Mendoza", "martin2@gmail.com", "2A")
e5 = Estudiante(1, "Max", "Tapia", "max_123@gmail.com", "2B")
e6 = Estudiante(1, "Eugenio", "Garrido", "eug.ga@gmail.com", "3A")
e7 = Estudiante(1, "Maria", "Castro", "cast_m@gmail.com", "3B")
e8 = Estudiante(1, "Lucia", "Castillo", "lucia_c@gmail.com", "3C")
e9 = Estudiante(1, "Valentina", "Figueroa", "valen@gmail.com", "4A")
e10 = Estudiante(1, "Samara", "Huaman", "sam@gmail.com", "5A")

cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [e1._id, e1.nombre, e1.apellido, e1.email, e1.seccion])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [e2._id, e2.nombre, e2.apellido, e2.email, e2.seccion])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [e3._id, e3.nombre, e3.apellido, e3.email, e3.seccion])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [e4._id, e4.nombre, e4.apellido, e4.email, e4.seccion])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [e5._id, e5.nombre, e5.apellido, e5.email, e5.seccion])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [e6._id, e6.nombre, e6.apellido, e6.email, e6.seccion])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [e7._id, e7.nombre, e7.apellido, e7.email, e7.seccion])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [e8._id, e8.nombre, e8.apellido, e8.email, e8.seccion])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [e9._id, e9.nombre, e9.apellido, e9.email, e9.seccion])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [e10._id, e10.nombre, e10.apellido, e10.email, e10.seccion])


cursor.execute("SELECT * FROM %s" % table_name)
estudiantes = cursor.fetchall()

print(" ESTUDIANTES ")
for row in estudiantes:
    print(row)

table_name = 'curso'
cursor.execute("DROP TABLE IF EXISTS %s " % table_name )

cursor.execute("create table %s ( id int, tutor varchar(20), area varchar(20), credito int, seccion varchar(20) );" % table_name)


c1 = Curso(1, "Andrea", "matematica", 3, "1A")
c2 = Curso(1, "Julio", "historia", 3, "1A")
c3 = Curso(1, "Gerardo", "comunicacion", 4, "1B")
c4 = Curso(1, "Marcia", "matematica", 4, "1C")
c5 = Curso(1, "Jorge", "ingles", 3, "1B")
c6 = Curso(1, "Iris", "ciencia", 3, "2A")
c7 = Curso(1, "Pamela", "computacion", 2, "3A")
c8 = Curso(1, "Gilberto", "comunicacion", 4, "1A")
c9 = Curso(1, "Sandra", "arte", 2, "3B")
c10 = Curso(1, "Elisa", "educacion fisica", 1, "2A")




cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [c1._id, c1.tutor, c1.area, c1.creditos, c1.aula])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [c2._id, c2.tutor, c2.area, c2.creditos, c2.aula])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [c3._id, c3.tutor, c3.area, c3.creditos, c3.aula])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [c4._id, c4.tutor, c4.area, c4.creditos, c4.aula])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [c5._id, c5.tutor, c5.area, c5.creditos, c5.aula])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [c6._id, c6.tutor, c6.area, c6.creditos, c6.aula])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [c7._id, c7.tutor, c7.area, c7.creditos, c7.aula])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [c8._id, c8.tutor, c8.area, c8.creditos, c8.aula])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [c9._id, c9.tutor, c9.area, c9.creditos, c9.aula])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [c10._id, c10.tutor, c10.area, c10.creditos, c10.aula])


cursor.execute("SELECT * FROM %s" % table_name)
Cursos = cursor.fetchall()

print(" CURSOS ")
for row in Cursos:
    print(row)

table_name = 'sección'
cursor.execute("DROP TABLE IF EXISTS %s " % table_name )
cursor.execute("create table %s ( id int, aula varchar(20), tutor varchar(20), piso int, seccion varchar(20) );" % table_name)

s1 = Sección(1, "1.01", "Andrea", 1, "1A")
s2 = Sección(1, "1.02", "Jorge", 1, "1C")
s3 = Sección(1, "1.01", "Guillermo", 1, "1B")
s4 = Sección(1, "1.01", "Massiel", 1, "2C")
s5 = Sección(1, "1.01", "Julio", 2, "2B")
s6 = Sección(1, "1.01", "Iris", 2, "2A")
s7 = Sección(1, "1.01", "Pamela", 2, "3A")
s8 = Sección(1, "1.01", "Marcia", 3, "3B")
s9 = Sección(1, "1.01", "Sandra", 3, "4A")
s10 = Sección(1, "1.01", "Elisa", 3, "5A")


cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [s1._id, s1.aula, s1.tutor, s1.piso, s1.grado])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [s2._id, s2.aula, s2.tutor, s2.piso, s2.grado])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [s3._id, s3.aula, s3.tutor, s3.piso, s3.grado])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [s4._id, s4.aula, s4.tutor, s4.piso, s4.grado])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [s5._id, s5.aula, s5.tutor, s5.piso, s5.grado])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [s6._id, s6.aula, s6.tutor, s6.piso, s6.grado])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [s7._id, s7.aula, s7.tutor, s7.piso, s7.grado])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [s8._id, s8.aula, s8.tutor, s8.piso, s8.grado])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [s9._id, s9.aula, s9.tutor, s9.piso, s9.grado])
cursor.execute("insert into %s values (%%s, %%s, %%s, %%s, %%s)" % table_name, [s10._id, s10.aula, s10.tutor, s10.piso, s10.grado])

print(" SECCIONES ")
cursor.execute("SELECT * FROM %s" % table_name)
secciones = cursor.fetchall()

for row in secciones:
    print(row)



connect.commit()