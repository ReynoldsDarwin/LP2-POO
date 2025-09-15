class ParImpar:
    def __init__(self):
        self.numeros = []

    def verificarParImpar(self):
        print("Verifica si los números ingresados son pares, impares o nulos")
        print("-------------------------------------------------------------")
        print("Escribe números para verificar. Escribe 'fin' para terminar.")
        entrada = ""
        while entrada.lower() != "fin":
            entrada = input("Ingrese un número: ")
            if entrada.isdigit():
                self.numeros.append(int(entrada))
            elif entrada.lower() != "fin":
                print("Entrada inválida: Escriba un número o 'fin'.")

        print("\nResultados:")
        for numero in self.numeros:
            if numero == 0:
                print(f"{numero} es nulo")
            elif numero % 2 == 0:
                print(f"{numero} es par")
            else:
                print(f"{numero} es impar")

def main():
    parimpar= ParImpar()
    parimpar.verificarParImpar()

if __name__ == "__main__":
    main()