class Nota:
    def __init__(self, seguimiento, parcial, final):
        self.seguimiento = seguimiento
        self.parcial = parcial
        self.final = final

    def calcularPromedio(self):
        return (self.seguimiento + self.parcial + self.final) / 3