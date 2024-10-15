import random
from usuario import Usuario
from alumno import Alumno
from profesor import Profesor
from materia import Materia

# Almacenamiento simulado
usuarios = []


# Función para cargar usuarios desde el archivo .txt
def cargar_usuarios_desde_archivo():
    try:
        with open('usuarios.txt', 'r') as archivo:
            usuario_actual = None
            for linea in archivo.readlines():
                datos = linea.strip().split(", ")

                # Si es una línea de usuario
                if len(datos) == 5:
                    id_usuario, nombre, apellido, contrasena, tipo_usuario = datos

                    # Crear el usuario correspondiente
                    if tipo_usuario == "Alumno":
                        usuario_actual = Alumno(int(id_usuario), nombre, apellido, contrasena)
                    elif tipo_usuario == "Profesor":
                        usuario_actual = Profesor(int(id_usuario), nombre, apellido, contrasena)

                    usuarios.append(usuario_actual)

                # Si es una línea de materia y notas (solo aplicable para alumnos)
                elif len(datos) > 0 and usuario_actual and isinstance(usuario_actual, Alumno):
                    if datos[0].startswith("Materia"):
                        nombre_materia = datos[0].split(": ")[1]
                        notas = datos[1].split(": ")[1]
                        seguimiento, parcial, final = [float(nota.split(": ")[1]) for nota in notas.split(", ")]

                        # Crear la materia y asignar las notas
                        materia = Materia(nombre_materia, usuario_actual)
                        materia.asignarNota(seguimiento, parcial, final)
                        usuario_actual.materias.append(materia)

    except FileNotFoundError:
        print("El archivo de usuarios no existe. Se creará cuando se añadan usuarios nuevos.")


# Fábrica de usuarios para reducir acoplamiento
def fabrica_usuarios(nombre, apellido, contrasena, tipo_usuario):
    id_usuario = random.randint(1000, 9999)  # Simulación de ID único
    if tipo_usuario == "alumno":
        return Alumno(id_usuario, nombre, apellido, contrasena)
    elif tipo_usuario == "profesor":
        return Profesor(id_usuario, nombre, apellido, contrasena)
    else:
        raise ValueError("Tipo de usuario no válido")


# Función para crear un nuevo usuario, utilizando la fábrica de usuarios
def crear_usuario(nombre, apellido, contrasena, tipo_usuario):
    try:
        nuevo_usuario = fabrica_usuarios(nombre, apellido, contrasena, tipo_usuario)
        usuarios.append(nuevo_usuario)
        print(f"Usuario creado: {nuevo_usuario.visualizarUsuario()}")
        guardar_usuario_en_archivo(nuevo_usuario)  # Guardar en archivo
        return nuevo_usuario
    except ValueError as e:
        print(e)


# Función para guardar un usuario en un archivo .txt (incluyendo la contraseña)
def guardar_usuario_en_archivo(usuario):
    with open('usuarios.txt', 'a') as archivo:
        archivo.write(
            f"{usuario.id}, {usuario.nombre}, {usuario.apellido}, {usuario.contrasena}, {type(usuario).__name__}\n")
        # Si el usuario es un alumno, guardar sus materias y notas
        if isinstance(usuario, Alumno):
            for materia in usuario.materias:
                archivo.write(f"  Materia: {materia.nombre}, Notas: {materia.visualizarNotas()}\n")


# Función para actualizar un archivo .txt cuando se asignan notas
def guardar_notas_en_archivo(alumno):
    with open('usuarios.txt', 'a') as archivo:
        for materia in alumno.materias:
            archivo.write(
                f"{alumno.id}, {alumno.nombre}, {alumno.apellido}, Materia: {materia.nombre}, Notas: {materia.visualizarNotas()}\n")


# Función para validar el inicio de sesión (usando los datos del archivo)
def iniciar_sesion(nombre_usuario, contrasena):
    for usuario in usuarios:
        if usuario.nombreUsuario == nombre_usuario and usuario.contrasena == contrasena:
            print(f"Inicio de sesión exitoso. Bienvenido {usuario.nombre} {usuario.apellido}")
            return usuario
    print("Credenciales inválidas. Inténtalo de nuevo.")
    return None


# Función para asignar notas a una materia de un alumno
def asignar_notas(alumno, nombre_materia, seguimiento, parcial, final):
    for materia in alumno.materias:
        if materia.nombre == nombre_materia:
            materia.asignarNota(seguimiento, parcial, final)
            guardar_notas_en_archivo(alumno)  # Guardar notas en el archivo
            return
    print(f"El alumno {alumno.nombre} no está matriculado en la materia {nombre_materia}.")


# Funciones de menú específicas para mejorar cohesión
def gestionar_creacion_usuario():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    contrasena = input("Contraseña: ")
    tipo_usuario = input("Tipo de usuario (alumno/profesor): ").strip().lower()
    crear_usuario(nombre, apellido, contrasena, tipo_usuario)


def gestionar_inicio_sesion():
    nombre_usuario = input("Nombre de usuario: ")
    contrasena = input("Contraseña: ")
    return iniciar_sesion(nombre_usuario, contrasena)


def gestionar_menu_profesor(profesor):
    while True:
        print("1. Crear usuario alumno")
        print("2. Crear materia para un alumno")
        print("3. Asignar notas a un alumno")
        print("4. Visualizar materias de un alumno")
        print("20. Cerrar sesión")
        print("21. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            gestionar_creacion_usuario()

        elif opcion == "2":
            id_alumno = int(input("ID del alumno: "))
            alumno = next((u for u in usuarios if isinstance(u, Alumno) and u.id == id_alumno), None)
            if alumno:
                nombre_materia = input("Nombre de la materia: ")
                profesor.crearMateria(alumno, nombre_materia)
            else:
                print("Alumno no encontrado.")

        elif opcion == "3":
            id_alumno = int(input("ID del alumno: "))
            alumno = next((u for u in usuarios if isinstance(u, Alumno) and u.id == id_alumno), None)
            if alumno:
                nombre_materia = input("Nombre de la materia: ")
                seguimiento = float(input("Nota de seguimiento: "))
                parcial = float(input("Nota del parcial: "))
                final = float(input("Nota final: "))
                asignar_notas(alumno, nombre_materia, seguimiento, parcial, final)
            else:
                print("Alumno no encontrado.")

        elif opcion == "4":
            id_alumno = int(input("ID del alumno: "))
            alumno = next((u for u in usuarios if isinstance(u, Alumno) and u.id == id_alumno), None)
            if alumno:
                profesor.visualizarMaterias(alumno)
            else:
                print("Alumno no encontrado.")

        elif opcion == "20":
            print("Cerrando sesión...")
            return

        elif opcion == "21":
            print("Saliendo...")
            exit()

        else:
            print("Opción no válida.")


def gestionar_menu_alumno(alumno):
    while True:
        print("1. Ver materias matriculadas")
        print("2. Ver notas de las materias")
        print("20. Cerrar sesión")
        print("21. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            materias = alumno.leerMaterias()
            print("Materias matriculadas:", materias)

        elif opcion == "2":
            notas = alumno.leerNotas()
            for materia, notas_materia in notas.items():
                print(f"Materia: {materia}, Notas: {notas_materia}")

        elif opcion == "20":
            print("Cerrando sesión...")
            return

        elif opcion == "21":
            print("Saliendo...")
            exit()

        else:
            print("Opción no válida.")


# Menú principal mejorado
def menu():
    cargar_usuarios_desde_archivo()  # Cargar usuarios del archivo antes de empezar el menú
    while True:
        print("\n--- Sistema de Notas Académicas ---")
        print("1. Crear usuario")
        print("2. Iniciar sesión")
        print("20. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            gestionar_creacion_usuario()

        elif opcion == "2":
            usuario_activo = gestionar_inicio_sesion()
            if isinstance(usuario_activo, Profesor):
                gestionar_menu_profesor(usuario_activo)
            elif isinstance(usuario_activo, Alumno):
                gestionar_menu_alumno(usuario_activo)
            else:
                print("Tipo de usuario no reconocido.")

        elif opcion == "20":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


# Ejecutar el menú
menu()
