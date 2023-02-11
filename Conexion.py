import sqlite3 
from sqlite3 import Error

def conectar():
    try:
        conexion = sqlite3.connect("database.db")
        return conexion
    except Error as err:
        print("Ha ocurrido un error.")

def crear_tablas(conexion):
    cursor = conexion.cursor()
    sentencia_sql1= '''CREATE TABLE IF NOT EXISTS usuario'''