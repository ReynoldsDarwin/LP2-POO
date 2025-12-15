#Prinicipio S

class CalculadoraFactorial:
    def calcular(self):
        raise NotImplementedError("Debe implementar el estado de calcular")
    
#Prinicipio O y L

class FactorialNumero(CalculadoraFactorial):
    def __init__(self,numero):
        self.numero = numero
        
    def calcular(self):
        resultado = 1
        for i in range(1,self.numero+1):
            resultado *= i
        return resultado
    
#Principio D

class Aplicacion:
    def __init__(self,calculadora):
        self.calculadora = calculadora
    def ejecutar(self):
        resultado = self.calculadora.calcular()
        print(f"El factorial es: {resultado}")
        
def main():
    factorial = FactorialNumero(5)
    app = Aplicacion(factorial)
    app.ejecutar()
    
if __name__ == "__main__":
    main()
        
        