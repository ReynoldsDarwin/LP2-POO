class SumaNaturales:
    def __init__(self, limite):
        self.limite = limite
        self.suma = 0  

    def calcularSuma(self):
        for i in range(1, self.limite + 1):
            self.suma += i
        return self.suma

def main():
    limite = int(input("Ingrese el n numeros primeros que desea sumar: "))
    miSuma = SumaNaturales(limite)
    resultado = miSuma.calcularSuma()
    print(f"La suma de los {limite} primeros números naturales es: {resultado}")

if __name__ == "__main__":
    main()
