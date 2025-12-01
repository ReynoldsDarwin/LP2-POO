import math

def calcular_hipotenusa(cateto_a, cateto_b):
    return math.sqrt(cateto_a**2 + cateto_b**2)

def main():
    try:
        a = float(input("Ingrese la longitud del cateto A: "))
        b = float(input("Ingrese la longitud del cateto B: "))
        
        if a <= 0 or b <= 0:
            raise ValueError("Los catetos deben ser números positivos.")
        
        hipotenusa = calcular_hipotenusa(a, b)
        print(f"La longitud de la hipotenusa es: {hipotenusa:.2f}")
    
    except ValueError as ve:
        print(f"Error de valor: {ve}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        
if __name__ == "__main__":
    main()