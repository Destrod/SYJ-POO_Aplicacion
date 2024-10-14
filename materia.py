# Clase Materia
class Materia:
    def __init__(self, nombre, alumno):
        self.nombre = nombre
        self.alumno = alumno
        self.notas = None  # Un objeto Nota asociado a la materia

    def asignarNota(self, seguimiento, parcial, final):
        self.notas = Nota(seguimiento, parcial, final)
        print(f"Notas asignadas en {self.nombre} para el alumno {self.alumno.nombre}")

    def visualizarAlumno(self):
        print(f"Alumno: {self.alumno.nombre} {self.alumno.apellido}")
        if self.notas:
            print(f"Notas - Seguimiento: {self.notas.seguimiento}, Parcial: {self.notas.parcial}, Final: {self.notas.final}, Promedio: {self.notas.calcularPromedio():.2f}")
        else:
            print("No hay notas asignadas para esta materia.")