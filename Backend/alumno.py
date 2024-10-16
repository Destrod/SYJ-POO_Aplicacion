# alumno.py
from usuario import Usuario

class Alumno(Usuario):
    def __init__(self, id, nombre, apellido, contrasena, nombre_usuario):
        super().__init__(id, nombre, apellido, contrasena)
        self.nombreUsuario = nombre_usuario  # Asignar el nombre de usuario específico del alumno
        self.materias = []  # Lista vacía de materias

    def leerMaterias(self):
        # Muestra las materias en las que está inscrito el alumno
        return [materia.nombre for materia in self.materias]

    def leerNotas(self):
        # Muestra las notas de las materias en las que está inscrito
        notas_materias = {}
        for materia in self.materias:
            notas_materias[materia.nombre] = materia.visualizarNotas()  # El alumno ve las notas asignadas
        return notas_materias