import numpy as np

class FiguraGeometrica:
    def __init__(self,nombre):
        self.nombre = nombre
    def area(self):
        raise NotImplementedError("Subclases deben implementar este método")
    def perimetro(self):
        raise NotImplementedError("Subclases deben implementar este método")
    
class Circulo(FiguraGeometrica):
    def __init__(self,radio):
        super() .__init__("Circulo")
        self.radio = radio
        
    def area(self):
        return np.pi * (self.radio**2)
    def perimetro(self):
        return 2*np.pi*self.radio
    
class Rectangulo(FiguraGeometrica):
    def __init__(self,base,altura):
        super() .__init__("Rectangulo")
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return 2*(self.base*self.altura)
        
circulo = Circulo(5)
print(f"Nombre: {circulo.nombre}")
print(f"Area: {circulo.area():.2f}")
print(f"Perimetro: {circulo.perimetro():.2f}")

rectangulo = Rectangulo(4,5)
print(f"Nombre: {rectangulo.nombre}")
print(f"Area: {rectangulo.area()}")
print(f"Perimetro: {rectangulo.perimetro()}")


        