import gc

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        print(f"\nProducto registrado: {self.nombre} - ${self.precio:.2f} en stock {self.cantidad}")

    def mostrar_informacion(self):
        print(f"{self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.cantidad}")

    def __del__(self):
        print(f"Producto eliminado: {self.nombre}")

productos = []

n = int(input("¿Cuántos productos va a ingresar?: "))

for i in range(n):
    print(f"\n--- Producto {i+1} ---")
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Stock del producto: "))

    producto = Producto(nombre, precio, cantidad)
    producto.mostrar_informacion()
    productos.append(producto)

del producto
productos.clear()
gc.collect()

print("\nFin del programa")
