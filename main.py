import random
from nota import Nota
from usuario import Usuario
from alumno import Alumno
from profesor import Profesor
from materia import Materia

# Almacenamiento simulado
usuarios = []

# Función para crear un nuevo usuario
def crearUsuario(nombre, apellido, contrasena, tipo_usuario):
    id_usuario = random.randint(1000, 9999)  # Simulación de ID único
    if tipo_usuario == "alumno":
        nuevo_usuario = Alumno(id_usuario, nombre, apellido, contrasena)
    elif tipo_usuario == "profesor":
        nuevo_usuario = Profesor(id_usuario, nombre, apellido, contrasena)
    else:
        print("Tipo de usuario no válido")
        return

    usuarios.append(nuevo_usuario)
    print(f"Usuario creado: {nuevo_usuario.visualizarUsuario()}")
    return nuevo_usuario

# Función para validar el inicio de sesión
def iniciar_sesion(nombre_usuario, contrasena):
    for usuario in usuarios:
        if usuario.nombreUsuario == nombre_usuario and usuario.validarUsuario(contrasena):
            print(f"Inicio de sesión exitoso. Bienvenido {usuario.nombre} {usuario.apellido}")
            return usuario
    print("Credenciales inválidas. Inténtalo de nuevo.")
    return None

# Función para asignar notas a una materia de un alumno
def asignar_notas(alumno, nombre_materia, seguimiento, parcial, final):
    for materia in alumno.materias:
        if materia.nombre == nombre_materia:
            materia.asignarNota(seguimiento, parcial, final)
            return
    print(f"El alumno {alumno.nombre} no está matriculado en la materia {nombre_materia}.")

# Menú interactivo
def menu():
    usuario_activo = None

    while True:
        if usuario_activo:
            print(f"\n--- Bienvenido, {usuario_activo.nombre} {usuario_activo.apellido} ---")
            if isinstance(usuario_activo, Profesor):
                print("1. Crear usuario alumno")
                print("2. Crear materia para un alumno")
                print("3. Asignar notas a un alumno")
                print("4. Visualizar materias de un alumno")
                print("5. Cerrar sesión")
                print("6. Salir")
            elif isinstance(usuario_activo, Alumno):
                print("1. Ver materias matriculadas")
                print("2. Cerrar sesión")
                print("3. Salir")
        else:
            print("\n--- Sistema de Notas Académicas ---")
            print("1. Crear usuario")
            print("2. Iniciar sesión")
            print("3. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1" and not usuario_activo:
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            contrasena = input("Contraseña: ")
            tipo_usuario = input("Tipo de usuario (alumno/profesor): ").strip().lower()
            crearUsuario(nombre, apellido, contrasena, tipo_usuario)

        elif opcion == "2" and not usuario_activo:
            nombre_usuario = input("Nombre de usuario: ")
            contrasena = input("Contraseña: ")
            usuario_activo = iniciar_sesion(nombre_usuario, contrasena)

        elif opcion == "3" and not usuario_activo:
            print("Saliendo...")
            break

        elif usuario_activo:
            if isinstance(usuario_activo, Profesor):
                if opcion == "1":
                    nombre = input("Nombre: ")
                    apellido = input("Apellido: ")
                    contrasena = input("Contraseña: ")
                    crearUsuario(nombre, apellido, contrasena, "alumno")

                elif opcion == "2":
                    id_alumno = int(input("ID del alumno: "))
                    alumno = next((u for u in usuarios if isinstance(u, Alumno) and u.id == id_alumno), None)
                    if alumno:
                        nombre_materia = input("Nombre de la materia: ")
                        usuario_activo.crearMateria(alumno, nombre_materia)
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
                        usuario_activo.visualizarMaterias(alumno)
                    else:
                        print("Alumno no encontrado.")

                elif opcion == "5":
                    print("Cerrando sesión...")
                    usuario_activo = None

                elif opcion == "6":
                    print("Saliendo...")
                    break

            elif isinstance(usuario_activo, Alumno):
                if opcion == "1":
                    materias = usuario_activo.leerMaterias()
                    print("Materias matriculadas:", materias)

                elif opcion == "2":
                    print("Cerrando sesión...")
                    usuario_activo = None

                elif opcion == "3":
                    print("Saliendo...")
                    break

        else:
            print("Opción no válida. Inténtalo de nuevo")

# Ejecutar el menú
menu()
