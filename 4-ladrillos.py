class Muro:
    def __init__(self, largo, alto, ancho, jv, jh):
        self.largo =  largo
        self.alto =  alto
        self.ancho =  ancho 
        self.jv = jv
        self.jh = jh
        
    def ladrillo_por_m2(self):
        area_ladrillo = (self.largo + self.jv) * (self.alto + self.jh)
        return 1/area_ladrillo
    
muro =  Muro(largo = 0.29, alto = 0.09, ancho = 0.13, jv=0.0015, jh=0.0015)

print("El area del muro es: ", muro.ladrillo_por_m2())

        