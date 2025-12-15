# Principio S
class Operacion:
    def operar(self, a, b):
        raise NotImplementedError("Debe implementar el método operar")

    def descripcion(self):
        raise NotImplementedError("Debe implementar el método descripcion")


# Principios O y L
class Suma(Operacion):
    def operar(self, a, b):
        return a + b

    def descripcion(self):
        return "suma"


class Resta(Operacion):
    def operar(self, a, b):
        return a - b

    def descripcion(self):
        return "resta"


class Multiplicacion(Operacion):
    def operar(self, a, b):
        return a * b

    def descripcion(self):
        return "multiplicacion"


class Division(Operacion):
    def operar(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        return a / b

    def descripcion(self):
        return "division"


# Principio D
class Calculadora:
    def __init__(self, operacion: Operacion):
        self.operacion = operacion

    def calcular(self, a, b):
        return self.operacion.operar(a, b)


def main():
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))

    operacion = Multiplicacion()
    calculadora = Calculadora(operacion)

    print(f"\n...Realizando una {operacion.descripcion()}...\n")
    resultado = calculadora.calcular(a, b)
    print(f"El resultado es: {resultado}")


if __name__ == "__main__":
    main()
