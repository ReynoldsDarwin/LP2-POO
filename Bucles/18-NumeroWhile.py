class Numeros:
    def __init__(self,cantidad):
        self.cantidad =  cantidad
        self.a = 0
        self.b = 1
        self.contador = 0

    def generarNumeros(self):
        print("Serie de Fibonacci")
        while self.contador <= self.cantidad:
            print(self.contador)
            self.contador += 1

def main():
    miNumeros = Numeros(10)
    miNumeros.generarNumeros()

if __name__=="__main__":
    main()




        