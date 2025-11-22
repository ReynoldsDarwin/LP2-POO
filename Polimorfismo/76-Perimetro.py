class Rectangulo:
    def perimetro(self, ancho, alto):
        return 2 * (ancho + alto)
    
class Circulo:
    def perimetro(self, radio):
        return 2 * 3.1416 * radio
    
class Triangulo:
    def perimetro(self, lado1, lado2, lado3):
        return lado1 + lado2 + lado3
    
figuras = [Rectangulo(), Circulo(), Triangulo()]

print("Perimetro del Rectangulo de base 4 y altura 5 es:", figuras[0].perimetro(4, 5))
print("Perimetro del Circulo de radio 3 es:", figuras[1].perimetro(3))
print("Perimetro del Triangulo de lados 3, 4 y 5 es:", figuras[2].perimetro(3, 4, 5))

