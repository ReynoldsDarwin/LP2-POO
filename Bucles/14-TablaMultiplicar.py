class TablaMultiplicar:
    def __init__(self, numero):
        self.numero = numero
        self.resultados = []

    def generarTabla(self):
        for i in range(1, 11):  
            self.resultados.append(f"{self.numero} x {i} = {self.numero * i}")
        return self.resultados

def main():
    numero = int(input("Ingrese el número para generar su tabla de multiplicar: "))
    miTabla = TablaMultiplicar(numero)
    resultado = miTabla.generarTabla()
    
    print("\nTabla de multiplicar del", numero)
    for linea in resultado:
        print(linea)

if __name__ == "__main__":
    main()
