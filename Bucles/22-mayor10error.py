class ValidadorNumero:
    def __init__(self):
        self.numero = None

    def pedir_numero(self):
        while True:
            entrada = input("Ingrese un número (máximo 10): ")
            try:
                self.numero = int(entrada)
                if self.numero > 10:
                    print("Error: El número no puede ser mayor que 10.")
                else:
                    print(f"Número ingresado correctamente: {self.numero}")
                    break
            except ValueError:
                print("Error: Debe ingresar un número válido.")

def main():
    validador = ValidadorNumero()
    validador.pedir_numero()

if __name__ == "__main__":
    main()