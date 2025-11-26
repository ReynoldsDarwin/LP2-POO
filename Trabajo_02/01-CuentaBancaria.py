class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: s/.{self.saldo}")
        else:
            print("El monto a depositar debe ser positivo")
    
    def retirar(self, monto):
        if monto <= 0:
            print("El monto a retirar debe ser positivo")
        elif self.saldo - monto < 0:
            print("Operación rechazada: fondos insuficientes")
        else:
            self.saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: s/.{self.saldo}")
    
    def mostrar_saldo(self):
        print(f"Titular: {self.titular}, Saldo: s/.{self.saldo}\n")
        
def main():
    print("\n===== Probando CuentaBancaria =====\n")
    cuenta1 = CuentaBancaria("Ana", 500)
    cuenta2 = CuentaBancaria("Luis",300)
    cuenta1.depositar(200)
    cuenta1.retirar(100)
    cuenta1.mostrar_saldo()

    cuenta2.retirar(500)
    cuenta2.mostrar_saldo()


if __name__ == "__main__":
    main()