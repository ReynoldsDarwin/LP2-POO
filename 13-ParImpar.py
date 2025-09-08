class ParImpar:
    def __init__(self, limite):
        self.limite = limite
        self.resultados = []

    def generar(self):
        for i in range(0, self.limite + 1):
            if i == 0:
                self.resultados.append(f"{i} es neutro")
            elif i % 2 == 0:
                self.resultados.append(f"{i} es par")
            else:
                self.resultados.append(f"{i} es impar")
        return self.resultados

def main():
    # limite = int(input("Ingrese el límite de números: "))
    miParImpar = ParImpar(10)
    resultado = miParImpar.generar()

    print("\nClasificación de números:")
    for linea in resultado:
        print(linea)

if __name__ == "__main__":
    main()