from usuario import Usuario

# Clase Profesor (hereda de Usuario)
class Profesor(Usuario):
    def __init__(self, id, nombre, apellido, contrasena):
        super().__init__()

    # Método para crear una nueva materia y asignarla a un alumno
    def crearMateria(self, alumno, nombre_materia):
        nueva_materia = Materia(nombre_materia, alumno)
        alumno.materias.append(nueva_materia)
        print(f"Materia '{nombre_materia}' creada y asignada al alumno {alumno.nombre} {alumno.apellido}")

    def visualizarMaterias(self, alumno):
        for materia in alumno.materias:
            print(f"Materia: {materia.nombre}")
            materia.visualizarAlumno()