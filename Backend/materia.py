from nota import Nota
class Materia:
    def __init__(self, nombre, alumno):
        self.nombre = nombre
        self.alumno = alumno
        self.notas = Nota()

    def visualizarNotas(self):
        # Devuelve las notas como un diccionario
        return {
            'seguimiento': self.notas.seguimiento,
            'parcial': self.notas.parcial,
            'final': self.notas.final
        }

    def asignarNota(self, seguimiento, parcial, final):
        # Asignar las notas directamente a los atributos del objeto Nota
        self.notas.seguimiento = seguimiento
        self.notas.parcial = parcial
        self.notas.final = final



