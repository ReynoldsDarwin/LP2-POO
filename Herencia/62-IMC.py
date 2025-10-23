class Peso:
    def __init__(self,peso_kg):
        self.peso_kg = peso_kg
        
class Altura:
    def __init__(self,altura_m):
        self.altura_m = altura_m
    
class Imc(Peso,Altura):
    def __init__(self, peso_kg, altura_m):
        Peso.__init__(self,peso_kg)   
        Altura.__init__(self,altura_m)
        
    def calcular_imc(self):
        if self.altura_m < 0:
            raise ValueError("La altura debe ser mayor a cero")
        return self.peso_kg/(self.altura_m**2)
    
    def categoria_imc(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            return "Bajo peso"
        elif 18.5 <= imc <25:
            return "normal"
        elif 25 <= imc <30:
            return "Sobrepeso"
        else:
            return "Obeso" 
        
    def mostrar_resultado(self):
        imc = self.calcular_imc() 
        categoria = self.categoria_imc()
        return f"IMC: {imc:.2f} Categoria: {categoria}"
    
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
            
peso = leer_float("Ingrese su peso en kilogramos: ")
altura = leer_float("Ingrese su altura en metros: ")            

persona = Imc(peso_kg=peso,altura_m=altura)
print(persona.mostrar_resultado())
 