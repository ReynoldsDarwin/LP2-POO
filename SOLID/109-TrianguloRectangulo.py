import math

# Principio S
class TrianguloRectangulo:
    def calcular(self):
        raise NotImplementedError("Debe implementar el método calcular hipotenusa.")


# Principio O y L
class Hipotenusa(TrianguloRectangulo):
    def __init__(self, cateto_a, cateto_b):
        self.cateto_a = cateto_a
        self.cateto_b = cateto_b 

    def calcular(self):
        return math.sqrt(self.cateto_a**2 + self.cateto_b**2) 
        


# Principio D
class Aplicacion:
    def __init__(self, calculadora):
        self.calculadora = calculadora

    def ejecutar(self):
        resultado = self.calculadora.calcular()
        print(f"La Hipotenusa del triangulo rectangulo es: {resultado}")


def main():
    hiptenusa = Hipotenusa(3, 4)
    app = Aplicacion(hiptenusa)
    app.ejecutar()


if __name__ == "__main__":
    main()
