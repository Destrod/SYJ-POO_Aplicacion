from usuario import Usuario
from alumno import Alumno
from profesor import Profesor
from materia import Materia
from nota import Nota

# Almacenamiento simulado
usuarios = []


# Función para cargar usuarios desde el archivo .txt
def cargar_usuarios_desde_archivo():
    try:
        with open('usuarios.txt', 'a+') as archivo:  # Modo 'a+' para crear si no existe
            archivo.seek(0)
            usuario_actual = None
            for linea in archivo.readlines():
                datos = linea.strip().split(", ")

                if len(datos) == 6:  # Incluye el nombre de usuario
                    id_usuario, nombre, apellido, contrasena, tipo_usuario, nombre_usuario = datos

                    if tipo_usuario == "Alumno":
                        usuario_actual = Alumno(int(id_usuario), nombre, apellido, contrasena, nombre_usuario)
                    elif tipo_usuario == "Profesor":
                        usuario_actual = Profesor(int(id_usuario), nombre, apellido, contrasena, nombre_usuario)

                    usuarios.append(usuario_actual)

                elif len(datos) > 0 and usuario_actual and isinstance(usuario_actual, Alumno):
                    if datos[0].startswith("Materia"):
                        nombre_materia = datos[0].split(": ")[1]
                        notas = datos[1].split(": ")[1]
                        seguimiento, parcial, final = [float(nota.split(": ")[1]) for nota in notas.split(", ")]

                        materia = Materia(nombre_materia, usuario_actual)
                        materia.asignarNota(seguimiento, parcial, final)
                        usuario_actual.materias.append(materia)

    except FileNotFoundError:
        print("El archivo de usuarios no existe. Se creará cuando se añadan usuarios nuevos.")


# Función para crear un nuevo profesor
def crear_profesor():
    try:
        id_profesor = int(input("ID del profesor: "))
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")

        while True:
            contrasena = input("Contraseña (6-10 caracteres): ")
            if 6 <= len(contrasena) <= 10:
                break
            print("La contraseña debe tener entre 6 y 10 caracteres. Inténtalo de nuevo.")

        nombre_usuario = f"{nombre.lower()}.{apellido.lower()}.admin{str(id_profesor)[-4:]}"
        nuevo_profesor = Profesor(id_profesor, nombre, apellido, contrasena, nombre_usuario)
        usuarios.append(nuevo_profesor)
        print(f"Profesor creado: {nuevo_profesor.visualizarUsuario()}")
        guardar_usuario_en_archivo(nuevo_profesor)
        return nuevo_profesor
    except ValueError as e:
        print(e)


# Función para crear un nuevo alumno
def crear_alumno():
    try:
        id_alumno = int(input("ID del alumno: "))
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")

        while True:
            contrasena = input("Contraseña (6-10 caracteres): ")
            if 6 <= len(contrasena) <= 10:
                break
            print("La contraseña debe tener entre 6 y 10 caracteres. Inténtalo de nuevo.")

        nombre_usuario = f"{nombre.lower()}.{apellido.lower()}.{str(id_alumno)[-4:]}"
        nuevo_alumno = Alumno(id_alumno, nombre, apellido, contrasena, nombre_usuario)
        usuarios.append(nuevo_alumno)
        print(f"Alumno creado: {nuevo_alumno.visualizarUsuario()}")
        guardar_usuario_en_archivo(nuevo_alumno)
        return nuevo_alumno
    except ValueError as e:
        print(e)


# Función para guardar un usuario en un archivo .txt
def guardar_usuario_en_archivo(usuario):
    with open('usuarios.txt', 'a+') as archivo:
        archivo.seek(0)
        contenido = archivo.read()
        if len(contenido) == 0:
            archivo.write("ID, Nombre, Apellido, Contraseña, Tipo de Usuario, Nombre de Usuario\n")  # Encabezados

        archivo.write(
            f"{usuario.id}, {usuario.nombre}, {usuario.apellido}, {usuario.contrasena}, {type(usuario).__name__}, {usuario.nombreUsuario}\n")

        if isinstance(usuario, Alumno):
            guardar_materias_al_archivo(usuario)
            guardar_notas_al_archivo(usuario)


# Función para guardar materias de un alumno en un archivo .txt
def guardar_materias_al_archivo(alumno):
    with open('materias.txt', 'a+') as archivo_materias:
        archivo_materias.seek(0)
        contenido = archivo_materias.read()
        if len(contenido) == 0:
            archivo_materias.write("ID Alumno, Nombre Alumno, Materia\n")
        for materia in alumno.materias:
            archivo_materias.write(f"{alumno.id}, {alumno.nombre}, {materia.nombre}\n")


# Función para guardar notas de un alumno en un archivo .txt
def guardar_notas_al_archivo(alumno):
    with open('notas.txt', 'a+') as archivo_notas:
        archivo_notas.seek(0)
        contenido = archivo_notas.read()
        if len(contenido) == 0:
            archivo_notas.write("ID Alumno, Nombre Alumno, Materia, Seguimiento, Parcial, Final\n")
        for materia in alumno.materias:
            notas = materia.visualizarNotas()  # Asegúrate de que es un diccionario
            archivo_notas.write(f"{alumno.id}, {alumno.nombre}, {materia.nombre}, {notas['seguimiento']}, {notas['parcial']}, {notas['final']}\n")


# Función para iniciar sesión
def iniciar_sesion(nombre_usuario, contrasena):
    for usuario in usuarios:
        if usuario is not None and usuario.nombreUsuario == nombre_usuario and usuario.contrasena == contrasena:
            print(f"Inicio de sesión exitoso. Bienvenido {usuario.nombre} {usuario.apellido}")
            return usuario
    print("Credenciales inválidas. Inténtalo de nuevo.")
    return None


# Función para gestionar el proceso de inicio de sesión
def gestionar_inicio_sesion():
    nombre_usuario = input("Nombre de usuario: ")
    contrasena = input("Contraseña: ")
    return iniciar_sesion(nombre_usuario, contrasena)


# Función para gestionar el menú del profesor
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
            crear_alumno()

        elif opcion == "2":
            id_alumno = int(input("ID del alumno: "))
            alumno = next((u for u in usuarios if isinstance(u, Alumno) and u.id == id_alumno), None)
            if alumno:
                nombre_materia = input("Nombre de la materia: ")
                materia = Materia(nombre_materia, alumno)
                alumno.materias.append(materia)
                guardar_materias_al_archivo(alumno)  # Guardar materia en archivo
                print(f"Materia '{nombre_materia}' creada y asignada al alumno {alumno.nombre}")
            else:
                print("Alumno no encontrado.")

        elif opcion == "3":
            id_alumno = int(input("ID del alumno: "))
            nombre_materia = input("Nombre de la materia: ")

            # Buscamos si el alumno está matriculado en la materia desde el archivo materias.txt
            with open('materias.txt', 'r') as archivo_materias:
                alumno_matriculado = False
                for linea in archivo_materias:
                    if f"{id_alumno}" in linea and nombre_materia in linea:
                        alumno_matriculado = True
                        break

            if alumno_matriculado:
                # Si está matriculado, creamos las notas
                alumno = next((u for u in usuarios if isinstance(u, Alumno) and u.id == id_alumno), None)
                if alumno:
                    nota = Nota()  # Aquí se crea la instancia de Nota con los valores predeterminados
                    nota.crearNota()  # Aquí se piden las 3 notas
                    materia = next((m for m in alumno.materias if m.nombre == nombre_materia), None)
                    if not materia:  # Si la materia no está en la lista del objeto alumno
                        materia = Materia(nombre_materia, alumno)  # Crear la materia
                        alumno.materias.append(materia)
                    materia.asignarNota(nota.seguimiento, nota.parcial, nota.final)
                    guardar_notas_al_archivo(alumno)  # Guardar notas en archivo
                    print(f"Notas asignadas para la materia {nombre_materia}")
                else:
                    print("El alumno no está en el sistema.")
            else:
                print(f"El alumno con ID {id_alumno} no está matriculado en la materia {nombre_materia}.")


        elif opcion == "4":
            id_alumno = int(input("ID del alumno: "))
            alumno = next((u for u in usuarios if isinstance(u, Alumno) and u.id == id_alumno), None)
            if alumno:
                for materia in alumno.materias:
                    print(f"Materia: {materia.nombre}, Notas: {materia.visualizarNotas()}")
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




# Función para gestionar el menú del alumno
def gestionar_menu_alumno(alumno):
    while True:
        print("\n--- Menú del Alumno ---")
        print("1. Ver materias matriculadas")
        print("2. Ver notas de una materia")
        print("20. Cerrar sesión")
        print("21. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            # Opción para ver materias matriculadas desde el archivo
            print("\nMaterias matriculadas:")
            with open('materias.txt', 'r') as archivo:
                materias_matriculadas = []
                for linea in archivo:
                    if f"{alumno.id}, {alumno.nombre}" in linea:
                        materia_nombre = linea.split(", ")[2].strip()
                        materias_matriculadas.append(materia_nombre)
                if materias_matriculadas:
                    for materia in materias_matriculadas:
                        print(f"Materia: {materia}")
                else:
                    print("No tienes materias matriculadas.")

        elif opcion == "2":
            # Opción para ver notas de una materia específica desde el archivo
            print("\nMaterias disponibles:")
            with open('notas.txt', 'r') as archivo:
                materias_disponibles = []
                for linea in archivo:
                    if f"{alumno.id}, {alumno.nombre}" in linea:
                        materias_disponibles.append(linea)
                if materias_disponibles:
                    for index, materia_info in enumerate(materias_disponibles, start=1):
                        print(f"{index}. {materia_info.split(', ')[2]}")

                    seleccion = int(input("Selecciona el número de la materia para ver las notas: "))
                    if 1 <= seleccion <= len(materias_disponibles):
                        materia_seleccionada = materias_disponibles[seleccion - 1]
                        print(f"Notas para {materia_seleccionada.split(', ')[2]}: {materia_seleccionada.split(', ')[3:]}")
                    else:
                        print("Selección no válida.")
                else:
                    print("No tienes materias matriculadas.")

        elif opcion == "20":
            print("Cerrando sesión...")
            return

        elif opcion == "21":
            print("Saliendo...")
            exit()

        else:
            print("Opción no válida. Inténtalo de nuevo.")


# Menú principal
def menu():
    cargar_usuarios_desde_archivo()
    while True:
        print("\n--- Sistema de Notas Académicas ---")
        print("1. Crear usuario profesor")
        print("2. Iniciar sesión")
        print("20. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            crear_profesor()

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


# Iniciar el programa
menu()
