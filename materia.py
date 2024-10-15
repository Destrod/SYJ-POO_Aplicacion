class Materia:
    def __init__(self, nombre, alumno):
        self.nombre = nombre
        self.alumno = alumno
        self.notas = []  # Lista de notas que podrían asignarse

    def asignarNota(self, seguimiento, parcial, final):
        # El profesor asigna las notas a la materia
        self.notas.append({'seguimiento': seguimiento, 'parcial': parcial, 'final': final})

    def visualizarAlumno(self):
        # Muestra información del alumno asignado a la materia
        print(f"Materia asignada a: {self.alumno.nombre} {self.alumno.apellido}")

    def visualizarNotas(self):
        # El alumno puede visualizar las notas asignadas por el profesor
        if self.notas:
            ultima_nota = self.notas[-1]  # Toma la última nota asignada
            return f"Seguimiento: {ultima_nota['seguimiento']}, Parcial: {ultima_nota['parcial']}, Final: {ultima_nota['final']}"
        else:
            return "No hay notas asignadas."
