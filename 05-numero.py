class Numero:
    def __init__(self,valor):
        self.valor =  valor
        
    def clasificar(self):
        if self.valor == 0:
            return "es nulo"
        elif self.valor % 2 == 0:
            return "es par"
        else:
            "es impar"
            
ejemplos =  [Numero(0), Numero(2), Numero(5)]

for num in ejemplos:
    tipo = num.clasificar()
    print(f"el numero ({num.valor}): {tipo}")
        
