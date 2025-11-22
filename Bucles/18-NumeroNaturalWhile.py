class NumeroNatural:
    def __init__(self, valor) :
        self.valor =  valor

    def mostrar(self):
        print(f"Numero natural: {self.valor}")

valor = int(input("Ingrese un numero entero: "))

def main():
    i = 1
    while i <=valor:
        numero = NumeroNatural(i)
        numero.mostrar()
        i+=1
if __name__ == "__main__":
    main()
        