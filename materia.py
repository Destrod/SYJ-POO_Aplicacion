class Materia:
    def __init__(self, id, nombre, alumno):
        self.ID = id
        self.nombre = nombre
        self.alumno = alumno
        self.notas = None

    def visualizarAlumno(self):
        print(f"Alumno: {self.alumno.nombre} {self.alumno.apellido}")

    def asignarNota(self, seguimiento, parcial, final):
        self.notas = Nota(seguimiento, parcial, final)

    def visualizarNotas(self):
        if self.notas:
            print(f"Notas - Seguimiento: {self.notas.seguimiento}, Parcial: {self.notas.parcial}, Final: {self.notas.final}, Promedio: {self.notas.calcularPromedio():.2f}")
        else:
            print("No hay notas asignadas para esta materia.")
