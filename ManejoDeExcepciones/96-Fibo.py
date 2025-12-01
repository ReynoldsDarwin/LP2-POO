def calcular_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("El número no puede ser negativo.")
    
    if n == 0:
        return 0

    a, b = 0, 1
    
    for _ in range(2, n + 1):
        a, b = b, a + b
        
    return b

def main() -> None:
    try:
        entrada = input("Ingrese un número entero para calcular su Fibonacci: ")
        
        try:
            num = int(entrada)
        except ValueError:
            print("Error: La entrada debe ser un número entero válido.")
            return

        resultado = calcular_fibonacci(num)
        print(f"Fibonacci de {num} es: {resultado}")

    except ValueError as ve:
        print(f"Error de dominio: {ve}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()