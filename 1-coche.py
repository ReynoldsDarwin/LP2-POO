class Coche:
    def __init__(self, marca, modelo, color):
        self.marca =  marca
        self.modelo =  modelo
        self.color = color
        
    def mostrar_info(self):
        print(f"Coche: {self.marca} {self.modelo} {self.color}")
        
    def arrancar(self):
        print(f"el coche de marca {self.marca} y modelo { self.modelo} arrancó")
        
marca = input("Ingrese marca del coche: ")
modelo =  input("Ingrese modelo del coche: ")
color =  input("Ingrese color del coche: ")

mi_coche = Coche(marca,modelo,color)

mi_coche.mostrar_info()
mi_coche.arrancar()
    