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


import tkinter as tk
from time import sleep

class TorresDeHanoiAnimado:
    
    def __init__(self, num_discos, canvas, root):
        self.num_discos = num_discos
        self.torres = [list(range(num_discos, 0, -1)), [], []]
        self.canvas = canvas
        self.root = root
        self.movimientos = 0
        
    def mover_disco(self, origen, destino):
        disco = self.torres[origen].pop()
        self.torres[destino].append(disco)
        self.movimientos += 1
        self.mostrar_estado()
        self.root.update()
        sleep(0.5)
        
    def resolver(self, n, origen, destino, auxiliar):
        if n == 1:
            self.mover_disco(origen, destino)
        else:
            self.resolver(n - 1, origen, auxiliar, destino)
            self.mover_disco(origen, destino)
            self.resolver(n - 1, auxiliar, destino, origen)
            
    def mostrar_estado(self):
        self.canvas.delete("all")
        
        ancho_canvas = 600
        alto_canvas = 400
        base_y = 350
        torre_x = [100, 300, 500]
        
        for i in range(3):
            self.canvas.create_rectangle(torre_x[i] - 5, 150, torre_x[i] + 5, base_y, fill="brown")
            self.canvas.create_rectangle(torre_x[i] - 80, base_y, torre_x[i] + 80, base_y + 10, fill="brown")
        
        ancho_max = 70
        ancho_min = 20
        alto_disco = 20
        
        for i, torre in enumerate(self.torres):
            for j, disco in enumerate(torre):
                ancho = ancho_min + (ancho_max - ancho_min) * (disco / self.num_discos)
                x1 = torre_x[i] - ancho
                x2 = torre_x[i] + ancho
                y1 = base_y - (j + 1) * alto_disco
                y2 = base_y - j * alto_disco
                
                color = f"#{255 - disco * 30:02x}{100 + disco * 20:02x}{150:02x}"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black", width=2)
        
        self.canvas.create_text(300, 30, text=f"Movimientos: {self.movimientos}", font=("Arial", 16, "bold"))

def main():
    root = tk.Tk()
    root.title("Torres de Hanoi")
    root.geometry("600x450")
    
    canvas = tk.Canvas(root, width=600, height=400, bg="white")
    canvas.pack()
    
    num_discos = 4
    hanoi = TorresDeHanoiAnimado(num_discos, canvas, root)
    hanoi.mostrar_estado()
    
    def iniciar_resolucion():
        hanoi.resolver(num_discos, 0, 2, 1)
    
    btn = tk.Button(root, text="Resolver", command=iniciar_resolucion, font=("Arial", 12))
    btn.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()