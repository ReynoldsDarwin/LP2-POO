class CalculadoraSuma:
    def __init__(self):
        self.total = 0

    def SumaNumeros(self):
        print("Calcula la suma de numeros ingresados")
        print("-------------------------------------")
        print("Escribe numeros para sumar. Escribe 'fin' para terminar.")
        entrada = ""
        while entrada.lower() != "fin":
            entrada = input("Ingrese un numero: ")
            if entrada.isdigit():
                self.total+= int(entrada)
            
            elif entrada.lower() != "fin":
                print("Entrada es invalida: Escriba un numero o 'fin' ")
        
        print(f"La suma total es: {self.total}")

def main():
    calculadora = CalculadoraSuma()
    calculadora.SumaNumeros()

if __name__ == "__main__":
    main()