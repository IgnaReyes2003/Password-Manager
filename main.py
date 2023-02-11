import os
from getpass import getpass 
from tabulate import tabulate
from Conexion import *

conexion = conectar()
crear_tablas(conexion)