import hashlib
from Conexion import *

def comprobar_usuario():
    conexion = conectar()
    cursor = conexion.cursor()
    sentencia_sql = "SELECT * FROM usuario"
    cursor.execute(sentencia_sql)
    usuario_encontrado = cursor.fetchall()
    conexion.close()
    return usuario_encontrado

def registrar(nombre, apellido, contrasena_maestra):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''INSERT INTO usuario
        (nombre, apellido, contrasena_maestra) 
        VALUES (?, ?, ?)'''
        cm_cifrada = hashlib.sha256(contrasena_maestra.encode("utf-8")).hexdigest()
        datos = (nombre, apellido, cm_cifrada)
        cursor.execute(sentencia_sql, datos)
        conexion.commit()
        conexion.close()
        return "Registro correcto"

    except Error as err:
        return "Ha ocurrido un error "+str(err)

def comprobar_contrasena(id, contrasena_maestra):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''SELECT * FROM usuario WHERE id=? AND contrasena_maestra=?'''
        cm_cifrada = hashlib.sha256(contrasena_maestra.encode("utf-8")).hexdigest()
        cursor.execute(sentencia_sql, (id, cm_cifrada))
        datos = cursor.fetchall()
        conexion.close()
        return datos
    except Error as err:
        return "Ha ocurrido un error "+ str(err)

