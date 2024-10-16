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
                        # Crear el nombre de usuario con los últimos 4 dígitos del ID
                        nombre_usuario = str(id_usuario)[-4:]
                        usuario_actual = Alumno(int(id_usuario), nombre, apellido, contrasena, nombre_usuario)
                    elif tipo_usuario == "Profesor":
                        # Crear el nombre de usuario del profesor con nombre.apellido.adminID
                        nombre_usuario = f"{nombre.lower()}.{apellido.lower()}.admin{str(id_usuario)[-4:]}"
                        usuario_actual = Profesor(int(id_usuario), nombre, apellido, contrasena, nombre_usuario)

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
        print("El archivo de usuarios no existe. Se creara cuando se agreguen usuarios nuevos.")

# Fábrica de usuarios para reducir acoplamiento (ahora se solicita el ID por consola)
def fabrica_usuarios(id_usuario, nombre, apellido, contrasena, tipo_usuario):
    # Extraer los últimos 4 dígitos del ID
    ultimos_cuatro_digitos = str(id_usuario)[-4:]

    if tipo_usuario == "alumno":
        # Generar el nombre de usuario para el alumno como nombre.apellidoID
        nombre_usuario = f"{nombre.lower()}.{apellido.lower()}.{ultimos_cuatro_digitos}"
        return Alumno(id_usuario, nombre, apellido, contrasena, nombre_usuario)
    elif tipo_usuario == "profesor":
        # Generar el nombre de usuario para el profesor como nombre.apellido.adminID
        nombre_usuario = f"{nombre.lower()}.{apellido.lower()}.admin{ultimos_cuatro_digitos}"
        return Profesor(id_usuario, nombre, apellido, contrasena, nombre_usuario)
    else:
        raise ValueError("Tipo de usuario no valido")


# Función para crear un nuevo profesor (ahora se solicita el ID y valida la longitud de la contraseña)
def crear_profesor():
    try:
        id_profesor = int(input("ID del profesor: "))  # Solicitar ID por consola
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")

        # Validar que la contraseña tenga entre 6 y 10 caracteres
        while True:
            contrasena = input("Contrasena (6-10 caracteres): ")
            if 6 <= len(contrasena) <= 10:
                break
            print("La contrasena debe tener entre 6 y 10 caracteres. Intentalo de nuevo.")

        nuevo_profesor = fabrica_usuarios(id_profesor, nombre, apellido, contrasena, "profesor")
        usuarios.append(nuevo_profesor)
        print(f"Profesor creado: {nuevo_profesor.visualizarUsuario()}")
        guardar_usuario_en_archivo(nuevo_profesor)  # Guardar en archivo
        return nuevo_profesor
    except ValueError as e:
        print(e)


# Función para crear un nuevo alumno (ahora se solicita el ID y valida la longitud de la contraseña)
def crear_alumno():
    try:
        id_alumno = int(input("ID del alumno: "))  # Solicitar ID por consola
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")

        # Validar que la contraseña tenga entre 6 y 10 caracteres
        while True:
            contrasena = input("Contrasena (6-10 caracteres): ")
            if 6 <= len(contrasena) <= 10:
                break
            print("La contrasena debe tener entre 6 y 10 caracteres. Intentalo de nuevo.")

        nuevo_alumno = fabrica_usuarios(id_alumno, nombre, apellido, contrasena, "alumno")
        usuarios.append(nuevo_alumno)
        print(f"Alumno creado: {nuevo_alumno.visualizarUsuario()}")
        guardar_usuario_en_archivo(nuevo_alumno)  # Guardar en archivo
        return nuevo_alumno
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
            print(f"Inicio de sesion exitoso. Bienvenido {usuario.nombre} {usuario.apellido}")
            return usuario
    print("Credenciales invalidas. Intentalo de nuevo.")
    return None


# Función para gestionar el proceso de inicio de sesión
def gestionar_inicio_sesion():
    nombre_usuario = input("Nombre de usuario: ")
    contrasena = input("Contrasena: ")
    return iniciar_sesion(nombre_usuario, contrasena)


# Función para asignar notas a una materia de un alumno
def asignar_notas(alumno, nombre_materia, seguimiento, parcial, final):
    for materia in alumno.materias:
        if materia.nombre == nombre_materia:
            materia.asignarNota(seguimiento, parcial, final)
            guardar_notas_en_archivo(alumno)  # Guardar notas en el archivo
            return
    print(f"El alumno {alumno.nombre} no está matriculado en la materia {nombre_materia}.")


# Modificar la función de gestión del menú del profesor
def gestionar_menu_profesor(profesor):
    while True:
        print("1. Crear usuario alumno")
        print("2. Crear materia para un alumno")
        print("3. Asignar notas a un alumno")
        print("4. Visualizar materias de un alumno")
        print("20. Cerrar sesion")
        print("21. Salir")

        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            crear_alumno()  # Usamos la nueva función para crear alumnos

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
            print("Cerrando sesion...")
            return

        elif opcion == "21":
            print("Saliendo...")
            exit()

        else:
            print("Opcion no valida.")


# Función para gestionar el menú del alumno
def gestionar_menu_alumno(alumno):
    while True:
        print("1. Ver materias matriculadas")
        print("2. Ver notas de las materias")
        print("20. Cerrar sesion")
        print("21. Salir")

        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            materias = alumno.leerMaterias()
            print("Materias matriculadas:", materias)

        elif opcion == "2":
            notas = alumno.leerNotas()
            for materia, notas_materia in notas.items():
                print(f"Materia: {materia}, Notas: {notas_materia}")

        elif opcion == "20":
            print("Cerrando sesion...")
            return

        elif opcion == "21":
            print("Saliendo...")
            exit()

        else:
            print("Opción no valida.")


# Menú principal mejorado
def menu():
    cargar_usuarios_desde_archivo()  # Cargar usuarios del archivo antes de empezar el menú
    while True:
        print("\n--- Sistema de Notas Academicas ---")
        print("1. Crear usuario profesor")
        print("2. Iniciar sesion")
        print("20. Salir")

        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            crear_profesor()  # Solo crear profesores aquí

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
            print("Opcion no valida. Intentalo de nuevo.")

menu()