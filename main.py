import os
from getpass import getpass 
from tabulate import tabulate
from Conexion import *

conexion = conectar()
crear_tablas(conexion)

def menu():
    while True:
        print("Seleccione una de las siguientes opciones: ")
        print("\t1- Añadir contraseña")
        print("\t2- Ver todas las contraseñas")
        print("\t3- Visualizar una contraseña")
        print("\t4- Modificar contraseña")
        print("\t5- Eliminar contraseña")
        print("\t6- Salir del programa")
        opcion = input("Seleccione una opción:")
        if opcion == "1":
            print("funciona")
        elif opcion == "2":
            print("funciona")
        elif opcion == "3":
            print("funciona")
        elif opcion == "4":
            print("funciona")
        elif opcion == "5":
            print("funciona")
        elif opcion == "6":
            break
        else: 
            print("Por favor, seleccione una de las opciones propuestas anteriormente.")
            
menu()