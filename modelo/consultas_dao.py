from .connecciondb import Conneccion

def crear_tabla():
    conn = Conneccion()
    sql = '''
        CREATE TABLE IF NOT EXISTS Cursos (
            idCurso INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            nombre VARCHAR(100) NOT NULL,
            nivel VARCHAR(100),
            turno VARCHAR(100) NOT NULL
        );

        CREATE TABLE IF NOT EXISTS Alumnos ( 
            idAlumno INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            nombre VARCHAR(100) NOT NULL,
            apellido VARCHAR(100) NOT NULL,
            mail VARCHAR(50) NOT NULL,
            direccion VARCHAR(100),
            idCurso INT,
            FOREIGN KEY (idCurso) REFERENCES Cursos (idCurso)
        );

        CREATE TABLE IF NOT EXISTS Notas (
            idNota INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            idAlumno INT,
            idCurso INT,
            nota DECIMAL(10,2),
            FOREIGN KEY (idAlumno) REFERENCES Alumnos (idAlumno),
            FOREIGN KEY (idCurso) REFERENCES Cursos (idCurso)
        );          
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error al crear las tablas: {e}")

class Alumno:
    def __init__(self, nombre, apellido, mail, direccion, idCurso):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.direccion = direccion
        self.idCurso = idCurso

    def __str__(self):
        return f'Alumno[{self.nombre}, {self.apellido}, {self.mail}, {self.direccion}, {self.idCurso}]'

def guardar_alumno(alumno):
    conn = Conneccion()
    sql = f'''
        INSERT INTO Alumnos (nombre, apellido, mail,direccion, idCurso)
        VALUES ('{alumno.nombre}', '{alumno.apellido}', '{alumno.mail}','{alumno.direccion}', {alumno.idCurso});
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error al guardar el alumno: {e}")

def listar_alumnos():
    conn = Conneccion()
    lista_alumnos = []

    sql = '''
        SELECT a.idAlumno, a.nombre, a.apellido, a.mail,a.direccion, a.idCurso, c.nombre AS curso, c.turno
        FROM Alumnos AS a
        LEFT JOIN Cursos AS c
        ON a.idCurso = c.idCurso;
    '''
    try:
        conn.cursor.execute(sql)
        alumnos = conn.cursor.fetchall()
        conn.cerrar_con()

        for a in alumnos:
            lista_alumnos.append({
                'id': a[0],
                'nombre': a[1],
                'apellido': a[2],
                'mail': a[3],
                'direccion': a[4],
                'idCurso': a[5],
                'curso': a[6],
                'turno': a[7]
            })

        return lista_alumnos
    except Exception as e:
        print(f"Error al listar los alumnos: {e}")
        return []

def editar_alumno(alumno, id):
    conn = Conneccion()
    sql = f'''
        UPDATE Alumnos
        SET nombre = '{alumno.nombre}', apellido = '{alumno.apellido}', mail = '{alumno.mail}', direccion = '{alumno.direccion}', idCurso = {alumno.idCurso}
        WHERE idAlumno = {id};
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error al editar el alumno: {e}")

def borrar_alumno(id):
    conn = Conneccion()
    sql = f'''
        DELETE FROM Alumnos
        WHERE idAlumno = {id};
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error al borrar el alumno: {e}")


