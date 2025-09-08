class Pitagoras:
    def __init__(self, catetoa, catetob):
        self.catetoa = catetoa
        self.catetob =  catetob
        
    def calcular_hipotenusa(self):
        return(self.catetoa**2 + self.catetob**2)**(1/2)
    
catetoa = float(input("Ingrese valor del cateto a: "))
catetob =  float(input("Ingrese valor del cateto b: "))

operacion =  Pitagoras(catetoa,catetob)

print("La hipotenusa es: ",operacion.calcular_hipotenusa())
    
        
    
        
        
