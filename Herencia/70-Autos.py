class VehiculoTerrestre:
    def conducir(self):
        print("Conduciendo por la carretera")
    def frenar(self):
        print("El vehiculo terrestre se ha detenido")
        
class VehiculoAcuatico:
    def navegar(self):
        print("Navegando por el agua")
    def fondear(self):
        print("El vehiculo acuatico ha fondeado\n")
        
class VehiculoAnfibio(VehiculoTerrestre,VehiculoAcuatico):
    def transformar(self,modo):
        if modo == "tierra":
            print("\nCambiando al modo terrestre")
        elif modo == "Agua":
            print("Cambiando al modo acuatico")
        else:
            print("Modo no reconocido")
            
def main():
    anfibio = VehiculoAnfibio()
    anfibio.transformar("tierra")
    anfibio.conducir()
    anfibio.frenar()
    
    print("\n")
    
    anfibio = VehiculoAnfibio()
    anfibio.transformar("Agua")
    anfibio.navegar()
    anfibio.fondear()
    
if __name__=="__main__":
    main()
            
            