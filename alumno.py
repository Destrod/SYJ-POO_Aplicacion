# Clase Alumno (hereda de Usuario)
from usuario import Usuario

class Alumno(Usuario):
    def __init__(self, id, nombre, apellido, contraseña):
        super().__init__(id, nombre, apellido, contraseña)
        self.materias = []  # Cada alumno puede tener varias materias

    def leerMaterias(self):
        if self.materias:
            return [materia.nombre for materia in self.materias]
        return "No está matriculado en ninguna materia."
