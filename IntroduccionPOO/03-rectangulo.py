class Rectangulo:
    def __init__(self, base, altura):
        self.base =  base
        self.altura =  altura
        
    def calcular_area(self):
        return self.base * self.altura
        
base = int(input("Ingrese tamaño de la base: "))
altura = int(input("Ingrese tamaño de la altura: "))

operacion =  Rectangulo(base,altura)

print("El área del rectangulo es: ",operacion.calcular_area())    


