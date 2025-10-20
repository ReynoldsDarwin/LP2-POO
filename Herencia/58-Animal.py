class Animal: #clase base o superclase
    def hacerSonido(self):
        print("Sonido genérico")
        
class Perro(Animal): #clase derivada o subclase
    def ladrar(self):
        print("!Guau¡")
        
        
perro = Perro()
perro.hacerSonido()
perro.ladrar()