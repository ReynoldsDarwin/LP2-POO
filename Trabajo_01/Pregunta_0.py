class Factorial:
    
    def __init__(self, numero):
        self.__numero = numero
    
    def calcular(self):
        if self.__numero < 0:
            return 
        
        factorial = 1
        for i in range(1, self.__numero + 1):
            factorial *= i
        return factorial
    
    def mostrar_resultado(self):

        resultado = self.calcular()
        print(f"El factorial de {self.__numero} es: {resultado}")

def main():
    factorial = Factorial(5)
    factorial.mostrar_resultado()  

if __name__ == "__main__":
    main()