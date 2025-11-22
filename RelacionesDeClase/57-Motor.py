class Motor:
    def __init__(self,tipo):
        self.tipo = tipo
    def encender(self):
        print(f"Motor: {self.tipo} encendido.")

class Auto:
    def __init__(self,marca):
        self.marca = marca
        self.motor = Motor("Electrico")
    def arrancar(self):
        print(f"Auto: {self.marca} arrancando")
        self.motor.encender()

miAuto = Auto("Tesla")
miAuto.arrancar()

        