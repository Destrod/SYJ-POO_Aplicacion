import random
from nota import Nota
from usuario import Usuario
from alumno import Alumno
from profesor import Profesor
from materia import Materia

# Almacenamiento simulado
usuarios = []

def crearUsuario(nombre, apellido, contrasena, tipo_usuario):
    id_usuario = random.randint(1000, 9999)  # Simulación de ID único
    if tipo_usuario == "alumno":
        nuevo_usuario = Alumno(id_usuario, nombre, apellido, contrasena)
    elif tipo_usuario == "profesor":
        nuevo_usuario = Profesor(id_usuario, nombre, apellido, contrasena)
    else:
        print("Tipo de usuario no valido")
        return

    usuarios.append(nuevo_usuario)
    print(f"Usuario creado: {nuevo_usuario.visualizarUsuario()}")
    return nuevo_usuario


def iniciar_sesion(nombre_usuario, contrasena):
    for usuario in usuarios:
        if usuario.nombreUsuario == nombre_usuario and usuario.validarUsuario(contrasena):
            print(f"Inicio de sesión exitoso. Bienvenido {usuario.nombre} {usuario.apellido}")
            return usuario
    print("Credenciales inválidas. Intentalo de nuevo.")
    return None

def asignar_notas(alumno, nombre_materia, seguimiento, parcial, final):
    for materia in alumno.materias:
        if materia.nombre == nombre_materia:
            materia.asignarNota(seguimiento, parcial, final)
            return
    print(f"El alumno no está matriculado en la materia {nombre_materia}.")

