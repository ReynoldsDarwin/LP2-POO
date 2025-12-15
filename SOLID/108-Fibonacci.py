# Principio S
class CalculadoraFibonacci:
    def calcular(self):
        raise NotImplementedError("Debe implementar el método calcular.")


# Principio O y L
class FibonacciNumero(CalculadoraFibonacci):
    def __init__(self, n):
        self.n = n

    def calcular(self):
        if self.n <= 0:
            return 0
        elif self.n == 1:
            return 1

        a, b = 0, 1
        for _ in range(2, self.n + 1):
            a, b = b, a + b
        return b


# Principio D
class Aplicacion:
    def __init__(self, calculadora):
        self.calculadora = calculadora

    def ejecutar(self):
        resultado = self.calculadora.calcular()
        print(f"El término Fibonacci es: {resultado}")


def main():
    fibonacci = FibonacciNumero(10)
    app = Aplicacion(fibonacci)
    app.ejecutar()


if __name__ == "__main__":
    main()
