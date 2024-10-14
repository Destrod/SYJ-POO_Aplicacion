# Clase Usuario
class Usuario:
    def __init__(self, id, nombre, apellido, contraseña):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.contraseña = contraseña
        self.nombreUsuario = self.generarNombreUsuario()

    def generarNombreUsuario(self):
        id_str = str(self.id).zfill(4)  # Asegura que el ID tenga al menos 4 dígitos
        return f"{self.nombre.lower()}{self.apellido.lower()}{id_str[-4:]}"  # Usar los últimos 4 dígitos del ID

    def visualizarUsuario(self):
        return {"id": self.id, "nombre": f"{self.nombre} {self.apellido}", "nombreUsuario": self.nombreUsuario}

    def validarUsuario(self, contraseña):
        return self.contraseña == contraseña
