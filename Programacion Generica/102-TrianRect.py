from typing import TypeVar, Generic
import math

T = TypeVar('T', int, float)

class TrianguloRectangulo(Generic[T]):
    def __init__(self,cateto_a, cateto_b,hipotenusa):
        self.cateto_a = cateto_a
        self.cateto_b = cateto_b
        self.hipotenusa = hipotenusa
        
    def calcular_hipotenusa(self, cateto_a: T, cateto_b: T) -> T:
        return math.sqrt(cateto_a**2 + cateto_b**2)
    
        
    def calcular_area_de_triagulo_rectangulo(self):
        return (self.cateto_a * self.cateto_b) / 2
    
    
    def calcular_perimetro_de_triangulo_rectangulo(self):
        hipotenusa = self.calcular_hipotenusa(self.cateto_a, self.cateto_b)
        return self.cateto_a + self.cateto_b + hipotenusa
    
def main():
    try:
        cateto_a = float(input("Ingrese la longitud del cateto a: "))
        cateto_b = float(input("Ingrese la longitud del cateto b: "))
        hipotenusa = TrianguloRectangulo.calcular_hipotenusa(None, cateto_a, cateto_b)
        
        triangulo = TrianguloRectangulo(cateto_a, cateto_b, hipotenusa)
        
        print(f"La hipotenusa calculada es: {triangulo.calcular_hipotenusa(cateto_a, cateto_b):.2f}")
        print(f"El área del triángulo rectángulo es: {triangulo.calcular_area_de_triagulo_rectangulo():.2f}")
        print(f"El perímetro del triángulo rectángulo es: {triangulo.calcular_perimetro_de_triangulo_rectangulo():.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    main()
        