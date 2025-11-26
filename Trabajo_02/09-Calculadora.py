class DivisionPorCeroError(Exception):
    pass

class CalculadoraSegura:
    def dividir(self, a: float, b: float) -> float:
        if b == 0:
            raise DivisionPorCeroError("Operación inválida: El divisor no puede ser cero.")
        return a / b

def main():
    calc = CalculadoraSegura()

    try:
        resultado = calc.dividir(10, 2)
        print(f"División exitosa: {resultado}")
        print("Intentando dividir por cero...")
        calc.dividir(5, 0)
        
    except DivisionPorCeroError as e:
        print(f"¡Excepción capturada! {e}")

if __name__ == "__main__":
    main()