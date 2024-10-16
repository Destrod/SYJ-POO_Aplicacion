class Nota:
    def __init__(self, seguimiento=None, parcial=None, final=None):
        self.seguimiento = seguimiento
        self.parcial = parcial
        self.final = final

    def calcularPromedio(self):
        return (self.seguimiento + self.parcial + self.final) / 3

    # Validación de las notas para asegurarse de que están entre 0 y 5
    def validarNota(self, mensaje):
        while True:
            try:
                valor = float(input(mensaje))
                if 0 <= valor <= 5:
                    return valor
                else:
                    print("La nota debe estar entre 0 y 5. Por favor, ingrese un valor válido.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

    def crearNota(self):
        # Pedir las notas y validarlas
        self.seguimiento = self.validarNota("Ingrese la nota de seguimiento (0-5): ")
        self.parcial = self.validarNota("Ingrese la nota del parcial (0-5): ")
        self.final = self.validarNota("Ingrese la nota final (0-5): ")
        print("Notas creadas")
