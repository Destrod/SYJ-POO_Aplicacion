class Usuario:
    def __init__(self, id, nombre, apellido, contrasena):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.contrasena = contrasena
        # Combina nombre, apellido y id para crear nombreUsuario
        self.nombreUsuario = f"{nombre.lower()}.{apellido.lower()}.{id}"

    def validarUsuario(self, contrasena):
        return self.contrasena == contrasena

    def visualizarUsuario(self):
        return {"id": self.id, "nombre": f"{self.nombre} {self.apellido}", "nombreUsuario": self.nombreUsuario}


# Función para crear un nuevo usuario pidiendo la ID como los últimos dígitos de la cédula
def crear_usuario():
    id_usuario = input("Introduce los ultimos 4 digitos de tu cedula: ")
    while not id_usuario.isdigit() or len(id_usuario) != 4:
        print("Por favor, introduce un numero valido de 4 digitos.")
        id_usuario = input("Introduce los ultimos 4 digitos de tu cedula: ")

    nombre = input("Introduce tu nombre: ")
    apellido = input("Introduce tu apellido: ")
    contrasena = input("Introduce tu contrasena: ")

    # Crear una instancia de Usuario con los datos proporcionados
    nuevo_usuario = Usuario(id_usuario, nombre, apellido, contrasena)

    print(f"Usuario creado: {nuevo_usuario.visualizarUsuario()}")
    return nuevo_usuario
