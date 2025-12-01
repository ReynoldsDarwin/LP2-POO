from typing import TypeVar
import math

T = TypeVar('T', int, float)

def calcular_hipotenusa(a: T, b: T) -> T:
    return math.sqrt(a**2 + b**2)

def main():
    cateto_a = float(input("Ingrese la longitud del cateto a: "))
    cateto_b = float(input("Ingrese la longitud del cateto b: "))

    print(f"{calcular_hipotenusa(cateto_a, cateto_b):.2f}")  

if __name__ == "__main__":
    main()