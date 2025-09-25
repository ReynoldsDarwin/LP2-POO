class CalculadoraEstadistica:
    def __init__(self, datos):
        self.datos = datos

    def media(self):    
        return sum(self.datos) / len(self.datos)
    
    def var(self):
        media = self.media()
        return sum((x - media)**2 for x in self.datos) / len(self.datos)
    
    def desviacionEstandar(self):
        return self.var() ** 0.5
    

def main():
    datos = input("Ingrese los datos separados por coma: ")
    datoslist = [float(x) for x in datos.split(",")]
    calculadora = CalculadoraEstadistica(datoslist)
    
    print(f"La media es: {calculadora.media()}.")
    print(f"La Varianza es: {calculadora.var()}.")
    print(f"La desviación estándar es: {calculadora.desviacionEstandar()}.")

    

if __name__ == "__main__":
    main()


        

    