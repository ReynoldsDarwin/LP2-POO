class Pitagoras:
    def __init__(self,catetoa,catetob):
        self.catetoa = catetoa
        self.catetob = catetob

    def calcular_hipo(self):
        return(self.catetoa**2 + self.catetob**2)**(1/2)
    
hipotenusa = Pitagoras(3,4)
print(hipotenusa.calcular_hipo())
    