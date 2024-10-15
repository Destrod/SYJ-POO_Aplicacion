from usuario import Usuario
from materia import Materia  # Asegúrate de que la ruta sea correcta

class Profesor(Usuario):
    def __init__(self, id, nombre, apellido, contrasena):
        # Inicializa manualmente los atributos y combina nombre, apellido e id
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.contrasena = contrasena
        # Combina nombre, apellido y id para crear nombreUsuario
        self.nombreUsuario = f"{nombre.lower()}.{apellido.lower()}.{id}"

    # Método para crear una nueva materia y asignarla a un alumno
    def crearMateria(self, alumno, nombre_materia):
        nueva_materia = Materia(nombre_materia, alumno)
        alumno.materias.append(nueva_materia)
        print(f"Materia '{nombre_materia}' creada y asignada al alumno {alumno.nombre} {alumno.apellido}")

    def visualizarMaterias(self, alumno):
        for materia in alumno.materias:
            print(f"Materia: {materia.nombre}")
            materia.visualizarAlumno()

    def visualizarMaterias(self, alumno):
        materias = alumno.leerMaterias()
        if materias:
            print(f"Materias de {alumno.nombre}: {', '.join(materias)}")
        else:
            print(f"El alumno {alumno.nombre} no está matriculado en ninguna materia.")
