from typing import TypeVar, Generic
import math

T = TypeVar('T')

class Figura(Generic[T]):
    def __init__(self,valor:T):
        self.valor =  valor
    def area(self)->float:
        pass
    def perimetro(self)->float:
        pass
        
class Rectangulo(Figura[float]):
    def __init__(self, base:float,altura:float):
        super().__init__(None)
        self.base = base
        self.altura = altura
        
    def area(self)->float:
        return self.base * self.altura
        
    def perimetro(self)->float:
        return (self.base + self.altura)*2
    
class Circulo(Figura[float]):
    def __init__(self, radio:float):
        super().__init__(None)
        self.radio = radio
        
    def area(self)->float:
        return math.pi * (self.radio**2)
    
    def perimetro(self)->float:
        return 2 * self.radio * math.pi
    
def main():
    rectagulo = Rectangulo(4,5)
    circulo = Circulo(3)
    
    print("\n====RECTANGULO====\n")
    print(f"Area: {rectagulo.area()}")
    print(f"Perimetro: {rectagulo.perimetro()}\n")
    
    print("====CIRCULO====\n")
    print(f"Area: {circulo.area():.2f}")
    print(f"Perimetro: {circulo.perimetro():.2f}\n")
    
if __name__=="__main__":
    main()
    