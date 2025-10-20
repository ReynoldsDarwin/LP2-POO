class Nadador: #clase base 1
    def nadar(self):
        print("Nadando en el agua")
    
class Volador: #clase base 2
    def volar(self):
        print("volando por el aire")
        
class Pato(Nadador,Volador):
    def graznar(self):
        print("!Cuak¡")

class Cisne(Nadador,Volador):
    def graznido(self):
        print("!oh-oh¡")
        
pato = Pato()
pato.nadar()
pato.volar()
pato.graznar()

cisne = Cisne()
cisne.nadar()
cisne.volar()
cisne.graznido()
