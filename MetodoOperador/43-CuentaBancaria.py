class CuentaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular 
        self.saldo = saldo

    def mostrar(self):
        print(f"Titular: {self.titular}, Saldo: ${self.saldo:.2f}")

    def __sub__(self,cantidad):
        if isinstance(cantidad,(int,float)):
            if cantidad <= self.saldo:
                return CuentaBancaria(self.titular, self.saldo-cantidad)
            else:
                print("Fondos Insuficientes")
                return self
        else:
            print("Operador no valido.")
            return self
        
titular = input("Ingrese su nombre: ")
saldo = float(input("Ingrese su saldo: "))
descuento1 = float(input("Ingrese el primer descuento: "))
descuento2 = float(input("Ingrese el segundo descuento: "))

cuenta1 = CuentaBancaria(titular,saldo)
cuenta1.mostrar()

cuenta2 = cuenta1 - descuento1
cuenta2.mostrar()

cuenta3 = cuenta2 - descuento2
cuenta3.mostrar()

