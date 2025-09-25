class Rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    def calcularArea(self):
        return self.base * self.altura
    
rect = Rectangulo(10,5)
print(f"El area del rectangulo es: ",rect.calcularArea())
      