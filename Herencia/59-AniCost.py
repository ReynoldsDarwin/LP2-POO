class Animal: #clase base o superclase
    def __init__(self,nombre):
        self.nombre = nombre
        
    def hacerSonido(self):
        pass
        
class Perro(Animal): #clase derivada o subclase
    def hacerSonido(self):
        return "!Guau¡"
    
class Gato(Animal):
    def hacerSonido(self):
        return "!Miau¡"
        
perro = Perro("Rex")
print(f"{perro.nombre} dice {perro.hacerSonido()}")

gato = Gato("Michi")
print(f"{gato.nombre} dice {gato.hacerSonido()}")