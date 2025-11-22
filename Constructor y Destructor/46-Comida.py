class Comida:
    def __init__(self,proteinas,carbohidratos,grasas):
        self.proteinas = proteinas
        self.carbohidratos = carbohidratos
        self.grasas = grasas
        print("Objeto comida creada")
        print(f"{self.proteinas}g {self.carbohidratos}g {self.grasas}g")

    def calcular_calorias(self):
        calorias = (self.proteinas*4) + (self.carbohidratos*4) + (self.grasas*9)
        return calorias
    
    def mostrar_informacion(self):
        print("INFORMACION NUTRICIONAL")
        print("-----------------------")
        print(f"Proteinas: {self.proteinas}g")
        print(f"Carbohidratos: {self.carbohidratos}g")
        print(f"Grasas: {self.grasas}g")
        print(f"Calorias totales: {self.calcular_calorias()}kcal")
        
almuerzo = Comida(proteinas=30,carbohidratos=50,grasas=20)
almuerzo.mostrar_informacion()

del almuerzo

try:
    almuerzo.mostrar_informacion()

except NameError:
    print("El objeto comida ya no existe")
