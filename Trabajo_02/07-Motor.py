class Motor:
    def encender(self):
        print("El motor se ha encendido.")

class Auto:
    def __init__(self):
        self.motor = Motor()

    def arrancar(self):
        print("Girando la llave del auto...")
        self.motor.encender()
        print("El vehiculo está listo para conducir.")

def main():
    mi_auto = Auto()
    mi_auto.arrancar()

if __name__ == "__main__":
    main()