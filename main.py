import os
from getpass import getpass 
from tabulate import tabulate
from Conexion import *
import Usuario
import Contrasena

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
            nueva_contrasena()
        elif opcion == "2":
            mostrar_contrasenas()
        elif opcion == "3":
            buscar_contrasena()
        elif opcion == "4":
            modificar_contrasena()
        elif opcion == "5":
            eliminar_contrasena()
        elif opcion == "6":
            break
        else: 
            print("Por favor, seleccione una de las opciones propuestas anteriormente.")

def nueva_contrasena():
    nombre = input("Ingrese el nombre: ")
    url= input("Ingrese una url: ")
    nombre_usuario= input("Ingrese el nombre de usuario: ")
    contrasena= input("Ingrese la contraseña: ")
    descripcion= input("Ingrese la descripción: ")
    respuesta= Contrasena.registrar(nombre, url, nombre_usuario, contrasena, descripcion)
    print(respuesta)

def mostrar_contrasenas():
    datos = Contrasena.mostrar()
    nuevos_datos= []
    headers = ["ID", "NOMBRE", "URL", "USUARIO", "CONTRASEÑA", "DESCRIPCIÓN"]

    for dato in datos:
        convertido = list(dato)
        convertido[4] ="********"
        nuevos_datos.append(convertido)

    tabla = tabulate(nuevos_datos, headers, tablefmt="fancy_grid")
    print("\t\t\t\tTodas las contraseñas")
    print(tabla)

def buscar_contrasena():
    contrasena_maestra = getpass("Ingrese su contraseña maestra: ")
    respuesta = Usuario.comprobar_contrasena(1, contrasena_maestra)
    if (len(respuesta)) == 0:
        print("Contraseña incorrecta")
    else:
        id = input("Ingrese el id de la contraseña a buscar: ")
        datos = Contrasena.buscar(id)
        headers = ["ID", "NOMBRE", "URL", "USUARIO", "CONTRASEÑA", "DESCRIPCIÓN"]
        tabla = tabulate(datos, headers, tablefmt="fancy_grid")
        print("\t\t\t\tTodas las contraseñas")
        print(tabla)

def modificar_contrasena():
    contrasena_maestra = getpass("Ingrese su contraseña maestra: ")
    respuesta = Usuario.comprobar_contrasena(1, contrasena_maestra)
    if (len(respuesta)) == 0:
        print("Contraseña incorrecta")
    else:
        id = input("Ingrese el id de la contraseña a modificar: ")
        nombre = input("Ingrese el nuevo nombre: ")
        url = input("Ingrese el nuevo url: ")
        nombre_usuario = input("Ingrese el nuevo nombre de usuario: ")
        contrasena = input("Ingrese la nueva contraseña: ")
        descripcion = input("Ingresa la nueva descripción: ")

        respuesta = Contrasena.modificar(id, nombre, url, nombre_usuario, contrasena, descripcion)
        print(respuesta)

def eliminar_contrasena():
    contrasena_maestra = getpass("Ingrese su contraseña maestra: ")
    respuesta = Usuario.comprobar_contrasena(1, contrasena_maestra)
    if (len(respuesta)) == 0:
        print("Contraseña incorrecta")
    else:
        id = input("Ingrese el id de la contraseña a eliminar: ")
        respuesta = Contrasena.eliminar(id)
        print(respuesta)

inicio()