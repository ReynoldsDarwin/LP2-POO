class Persona:
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad =  edad
        
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return f"{self.nombre} es mayor de edad."
        else:
            return f"{self.nombre} es menor de edad."
        
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

persona = Persona(nombre,edad)
print(persona.es_mayor_de_edad())
