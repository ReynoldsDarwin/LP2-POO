import math
class TrianguloRectangulo:
    def __init__(self,cateto_a,cateto_b): #constructor
        self.cateto_a = cateto_a
        self.cateto_b = cateto_b

    def calcular_Hipotenusa(self):
        hipotenusa = math.sqrt(self.cateto_a**2 + self.cateto_b**2)
        return hipotenusa
    
    def __del__(self):
        print("Objeto TrianguloRectangulo destruido")

def main():
    try:
        cateto1 = float(input("Ingrese en valor del primer cateto: "))
        cateto2 = float(input("Ingrese el valor del segundo cateto: "))

        triagulo = TrianguloRectangulo(cateto1,cateto2)
        resultado = triagulo.calcular_Hipotenusa()

        print(f"La hiptenusa del triangulo es: {resultado}")
    except NameError:
        print("El objeto triangulo ya no existe (fue destruido)")

if __name__=="__main__":
    main()
        