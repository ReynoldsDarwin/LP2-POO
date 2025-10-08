class CuentaBancaria:
    
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo
    
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo
    
    def mostrar_datos(self):
        print(f"Titular: {self.__titular} - Saldo: {self.__saldo}")

def main():
    cuenta = CuentaBancaria("Ana Pérez", 5000)
    cuenta.mostrar_datos()
    cuenta.set_saldo(7000)
    cuenta.mostrar_datos()
    cuenta.set_saldo(-100)

if __name__ == "__main__":
    main()