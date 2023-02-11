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
        cm_cifrada = hashlib.sha256(contrasena_maestra.encode("utf_8")).hexadigest()
        datos = nombre