'''class Materia:
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
            return "No hay notas asignadas." '''



from nota import Nota  # Importamos la clase Nota

class Materia:
    def __init__(self, nombre, alumno):
        self.nombre = nombre
        self.alumno = alumno
        self.notas = None  # Inicialmente no hay notas

    def asignarNota(self):
        # Crear una instancia de Nota y pedir las notas
        print(f"Asignando notas para la materia {self.nombre} del alumno {self.alumno.nombre} {self.alumno.apellido}")
        nota = Nota(0, 0, 0)  # Creamos una instancia de Nota con valores iniciales
        nota.crearNota()  # Utilizamos el método crearNota para pedir las notas al profesor
        self.notas = nota  # Asignar la instancia de Nota a la materia

    def visualizarAlumno(self):
        # Muestra información del alumno asignado a la materia
        print(f"Materia asignada a: {self.alumno.nombre} {self.alumno.apellido}")

    def visualizarNotas(self):
        # El alumno puede visualizar las notas asignadas por el profesor
        if self.notas:
            promedio = self.notas.calcularPromedio()  # Calcular el promedio de las notas
            return (f"Seguimiento: {self.notas.seguimiento}, Parcial: {self.notas.parcial}, Final: {self.notas.final}, "
                    f"Promedio: {promedio:.2f}")
        else:
            return "No hay notas asignadas."
