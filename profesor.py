from usuario import Usuario
from materia import Materia

# Clase Profesor (hereda de Usuario)
class Profesor(Usuario):
    def __init__(self, id, nombre, apellido, contrasena):
        super().__init__(id, nombre, apellido, contrasena)

    def crearMateria(self, alumno, nombre_materia):
        nueva_materia = Materia(nombre_materia, alumno)
        alumno.materias.append(nueva_materia)
        print(f"Materia '{nombre_materia}' creada y asignada al alumno {alumno.nombre} {alumno.apellido}")

    def visualizarMaterias(self, alumno):
        for materia in alumno.materias:
            print(f"Materia: {materia.nombre}")
            materia.visualizarAlumno()

    def modificarMaterias(self, alumno, nombre_materia, nuevo_nombre):
        for materia in alumno.materias:
            if materia.nombre == nombre_materia:
                materia.nombre = nuevo_nombre
                print(f"Materia '{nombre_materia}' modificada a '{nuevo_nombre}'")

    def eliminarMaterias(self, alumno, nombre_materia):
        alumno.materias = [materia for materia in alumno.materias if materia.nombre != nombre_materia]
        print(f"Materia '{nombre_materia}' eliminada")

    def eliminarUsuario(self, alumno):
        print(f"Eliminando alumno {alumno.nombre} {alumno.apellido}")
