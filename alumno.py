from usuario import Usuario

class Alumno(Usuario):
    def __init__(self, id, nombre, apellido, contrasena):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.contrasena = contrasena
        self.materias = []  # Lista vacía de materias
        # Combina nombre, apellido e id para crear nombreUsuario
        self.nombreUsuario = f"{nombre.lower()}.{apellido.lower()}.{id}"

    def leerMaterias(self):
        # Muestra las materias en las que está inscrito el alumno
        return [materia.nombre for materia in self.materias]

    def leerNotas(self):
        # Muestra las notas de las materias en las que está inscrito
        notas_materias = {}
        for materia in self.materias:
            notas_materias[materia.nombre] = materia.visualizarNotas()  # El alumno ve las notas asignadas
        return notas_materias
