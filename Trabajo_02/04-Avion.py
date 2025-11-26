class Vehiculo:
    def acelerar(self):
        print("El vehículo está acelerando en la pista.")

class Volador:
    def volar(self):
        print("La aeronave está volando muy alto.")

class Avion(Vehiculo, Volador):
    pass

def main():
    mi_avion = Avion()
    
    mi_avion.acelerar()
    mi_avion.volar()

if __name__ == "__main__":
    main()