class Nota:
    def __init__(self, seguimiento, parcial, final):
        self.seguimiento = seguimiento
        self.parcial = parcial
        self.final = final

    def calcularPromedio(self):
        return (self.seguimiento + self.parcial + self.final) / 3

    def editarNota(self, nuevo_seguimiento, nuevo_parcial, nuevo_final):
        self.seguimiento = nuevo_seguimiento
        self.parcial = nuevo_parcial
        self.final = nuevo_final
        print("Notas actualizadas")

    def crearNota(self, seguimiento, parcial, final):
        self.seguimiento = seguimiento
        self.parcial = parcial
        self.final = final
        print("Notas creadas")
