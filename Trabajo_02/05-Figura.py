import math

class Figura:
    def area(self):
        raise NotImplementedError

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

def main():
    figuras = [
        Rectangulo(10, 5),
        Triangulo(10, 5),
        Circulo(7)
    ]

    for figura in figuras:
        print(f"Área: {figura.area():.2f}")

if __name__ == "__main__":
    main()