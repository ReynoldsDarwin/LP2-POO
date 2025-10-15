import math

class Circulo:
    def __init__(self,radio):
        self.radio = radio

    def calcular_area(self):
        area = math.pi *self.radio**2
        return round(area,2)

    def calcular_per(self):
        per = 2 * math.pi * self.radio
        return round(per,2)
    
    def mostrar_info(self):
        print(f"Radio del circulo es: {self.radio}")
        print(f"El area es: {self.calcular_area()}")
        print(f"El perimetro es: {self.calcular_per()}")

circ = Circulo(5)
circ.mostrar_info()