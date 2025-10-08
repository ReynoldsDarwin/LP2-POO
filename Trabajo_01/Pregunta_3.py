class TorresDeHanoi:
    
    def __init__(self, num_discos):
        self.num_discos = num_discos
        self.torres = [list(range(num_discos, 0, -1)), [], []]
        self.movimientos = 0
        
    def mover_disco(self, origen, destino):
        disco = self.torres[origen].pop()
        self.torres[destino].append(disco)
        self.movimientos += 1
        self.mostrar_estado()
        
    def resolver(self, n, origen, destino, auxiliar):
        if n == 1:
            self.mover_disco(origen, destino)
        else:
            self.resolver(n - 1, origen, auxiliar, destino)
            self.mover_disco(origen, destino)
            self.resolver(n - 1, auxiliar, destino, origen)
            
    def mostrar_estado(self):
        print(f"\nMovimiento {self.movimientos}:")
        print(f"Torre 1: {self.torres[0]}")
        print(f"Torre 2: {self.torres[1]}")
        print(f"Torre 3: {self.torres[2]}")

def main():
    hanoi = TorresDeHanoi(4)
    print("Estado inicial:")
    hanoi.mostrar_estado()
    hanoi.resolver(4, 0, 2, 1)
    print(f"\nTotal de movimientos: {hanoi.movimientos}")

if __name__ == "__main__":
    main()