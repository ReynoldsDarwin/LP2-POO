class Persona:
    def __init__(self, nombre, peso, altura):
        self.nombre = nombre
        self.peso = peso      
        self.altura = altura  

    def calcular_imc(self):
        imc = self.peso / (self.altura**2)
        return imc

    def clasificar_imc(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            return "Bajo peso"
        elif 18.5 <= imc <= 24.9:
            return "Normal"
        elif 25.0 <= imc <= 29.9:
            return "Sobrepeso"
        elif 30.0 <= imc <= 34.9:
            return "Obesidad grado I"
        elif 35.0 <= imc <= 39.9:
            return "Obesidad grado II"
        else:
            return "Obesidad grado III (mórbida)"

persona = Persona("roberto", 51, 1.56)
print(f"{persona.nombre} tiene un IMC de {persona.calcular_imc():.2f}, esta en la clasificacion de: {persona.clasificar_imc()}")
