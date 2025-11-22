class Cateto_a:
    def __init__(self, a):
        self.a = a

class Cateto_b:
    def __init__(self, b):
        self.b = b

class Pitagoras(Cateto_a, Cateto_b):
    def __init__(self, a, b):
        Cateto_a.__init__(self, a)
        Cateto_b.__init__(self, b)

    def calcular_hipotenusa(self):
        return (self.a**2 + self.b**2) ** 0.5
    
def leer_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))      
            if valor <= 0:
                print("Por favor ingrese un valor positivo")
                continue
            return valor
        except ValueError:
            print("Entrada invalida, ingrese un numero valido")
a = leer_float("Ingrese la longitud del cateto a: ")
b = leer_float("Ingrese la longitud del cateto b: ")

teorema = Pitagoras(a, b)
hipotenusa = teorema.calcular_hipotenusa()
print(f"La longitud de la hipotenusa es: {hipotenusa:.2f}")