import math

# Principio S
class FiguraGeometrica:
    def calcularArea(self):
        raise NotImplementedError("Debe implementar el método calcularArea.")
    
    def calcularPerimetro(self):
        raise NotImplementedError("Debe implementar el método calcularPerimetro.")


# Principio O y L
class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcularArea(self):
        return math.pi * self.radio**2
    def calcularPerimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

    def calcularPerimetro(self):
        return 2 * (self.base + self.altura)
    
# Principio D

class Aplicacion:
    def __init__(self, figura):
        self.figura = figura

    def ejecutar(self):
        print(f"El área es: {self.figura.calcularArea():.2f}")
        print(f"El perímetro es: {self.figura.calcularPerimetro():.2f}")
        
radio_dato = float(input("Ingrese el radio del círculo: "))
base_dato = float(input("Ingrese la base del rectángulo: "))
altura_dato = float(input("Ingrese la altura del rectángulo: "))

def main():
    circulo = Circulo(radio_dato)
    rectangulo = Rectangulo(base_dato, altura_dato)
    app_circulo = Aplicacion(circulo)
    app_rectangulo = Aplicacion(rectangulo)
    app_circulo.ejecutar()
    app_rectangulo.ejecutar()
    
if __name__ == "__main__":
    main()