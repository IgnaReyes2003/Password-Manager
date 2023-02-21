import os
from getpass import getpass 
from tabulate import tabulate
from Conexion import *
import Usuario

conexion = conectar()
crear_tablas(conexion)

def inicio():
    os.system("cls")
    comprobar = Usuario.comprobar_usuario()
    if len(comprobar) == 0:
        print("Bienvenido, registre su información")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        contrasena_maestra = getpass("Ingrese su contraseña maestra: ")
        resultado = Usuario.registrar(nombre, apellido, contrasena_maestra)
        if resultado == "Registro correcto":
            print(f"Bienvenido {nombre}")
            menu()
        else:
            print(resultado)
    else: 
        contrasena_maestra = getpass("Ingrese su contraseña maestra: ")
        resultado = Usuario.comprobar_contrasena(1, contrasena_maestra)

        if len(resultado) == 0:
            print("Contraseña incorrecta")
        else:
            print("Contraseña correcta, Bienvenido")
            menu()

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

inicio()