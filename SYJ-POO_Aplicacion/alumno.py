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
            # Acceder al método visualizarNotas() de la clase Materia para obtener las notas del alumno
            notas_materias[materia.nombre] = materia.visualizarNotas()
        return notas_materias

    def visualizarNotasMaterias(self):
        # Este método imprime las notas de todas las materias inscritas
        if not self.materias:
            print("El alumno no tiene materias inscritas.")
        else:
            for materia in self.materias:
                print(f"Materia: {materia.nombre}")
                print(f"Notas: {materia.visualizarNotas()}")
