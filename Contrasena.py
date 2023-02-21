from Conexion import *

def registrar(nombre, url, nombre_usuario, contrasena, descripcion):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''INSERT INTO TABLE contrasena (
        nombre, url, nombre_usuario, contrasena, descripcion)
        VALUES (?, ?, ?, ?, ?)'''
        datos = (nombre, url, nombre_usuario, contrasena, descripcion)
        cursor.execute(sentencia_sql, datos)
        conexion.commit()
        conexion.close()
        return "Registro correcto"
    except Error as err:
        return "Ha ocurrido un error" + str(err)
    
def mostrar():
    datos = []
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''SELECT * FROM contrasena'''
        cursor.execute(sentencia_sql)
        datos = cursor.fetchall()
        conexion.close()
    except Error as err:
        print("Ha ocurrido un error "+str(err))
    return datos

def buscar(id):
    datos = []
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''SELECT * FROM contrasena WHERE id=?'''
        cursor.execute(sentencia_sql, (id,))
        datos = cursor.fetchall()
        conexion.close()
    except Error as err:
        print("Ha ocurrido un error "+str(err))
    return datos

def modificar(id, nombre, url, nombre_usuario, contrasena, descripcion):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''UPDATE contrasena SET nombre=?, url=?, 
        nombre_usuario=?, contrasena=?, descripcion=? WHERE id=?'''
        datos = (nombre, url, nombre_usuario, contrasena, descripcion, id)
        cursor.execute(sentencia_sql,datos)
        conexion.commit()
        conexion.close()
        return "Se mofidicó la contraseña"
    except Error as err:
        return "Ha ocurrido un error "+str(err)
    
def eliminar(id):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''DELETE FROM contrasena WHERE id=?'''
        cursor.execute(sentencia_sql,(id,))
        conexion.commit()
        conexion.close()
        return "Se eliminó la contraseña"
    except Error as err:
        return "Ha ocurrido un error "+str(err)