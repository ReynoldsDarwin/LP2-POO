class Calculadora:
    def __init__(self,a,b):
        self.a = a
        self.b = b


    def sumar(self):
        return self.a + self.b
    
calc = Calculadora(1,3)
print(f"La suma de los parametros: {calc.a} y {calc.b} es: ", calc.sumar())
    