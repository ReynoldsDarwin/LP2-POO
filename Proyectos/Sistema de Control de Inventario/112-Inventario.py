from abc import ABC, abstractmethod

#S

class Producto:
    """Representa únicamente los datos de un producto."""
    def __init__(self, id_p: int, nombre: str, cantidad: int, precio: float):
        self.id = id_p
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

# O - Open/Closed Principle (OCP) - El sistema está abierto a la extensión (nuevos tipos de inventario) 

class Inventario(ABC):
    """Interfaz abstracta para el manejo de datos."""
    @abstractmethod
    def guardar(self, producto: Producto): pass
    
    @abstractmethod
    def actualizar(self, id_p: int, cantidad: int): pass
    
    @abstractmethod
    def obtener_lista(self) -> list: pass

    @abstractmethod  
    def buscar_por_id(self, id_p: int) -> Producto: pass

# L - Liskov Substitution Principle (LSP)
# Podemos usar InventarioEnMemoria en lugar de RepositorioInventario 
# sin alterar el comportamiento esperado.

class InventarioEnMemoria(Inventario):
    def __init__(self):
        self._productos = {}

    def guardar(self, p: Producto):
        if p.id in self._productos:
            raise ValueError(f"ID {p.id} ya existe.")
        self._productos[p.id] = p

    def actualizar(self, id_p: int, cantidad: int):
        if id_p not in self._productos:
            raise KeyError("Producto no encontrado.")
        nuevo_stock = self._productos[id_p].cantidad + cantidad
        if nuevo_stock < 0:
            raise ValueError("Stock insuficiente.")
        self._productos[id_p].cantidad = nuevo_stock

    def obtener_lista(self):
        return list(self._productos.values())

    def buscar_por_id(self, id_p: int) -> Producto:  
        if id_p not in self._productos:
            raise KeyError("Código de barras no reconocido.")
        return self._productos[id_p]

#I

class GeneradorReportes:
    """Clase dedicada exclusivamente a formatear la salida de datos."""
    @staticmethod
    def imprimir_tabla(productos):
        print("\n{:<5} {:<20} {:<10} {:<10}".format("ID", "PRODUCTO", "STOCK", "PRECIO"))
        print("-" * 50)
        for p in productos:
            print(f"{p.id:<5} {p.nombre:<20} {p.cantidad:<10} s/. {p.precio:<10.2f}")

    @staticmethod
    def imprimir_resumen(productos):
        total_v = sum(p.cantidad * p.precio for p in productos)
        print("-" * 50)
        print(f"VALOR TOTAL DEL INVENTARIO: s/. {total_v:,.2f}")

    @staticmethod
    def mostrar_detalle_escaneo(p: Producto):  # NUEVO: Vista de escáner
        print("\n" + "="*30)
        print(f"{'LECTURA DE CÓDIGO':^30}")
        print("="*30)
        print(f"CÓDIGO: {p.id}")
        print(f"NOMBRE: {p.nombre}")
        print(f"STOCK : {p.cantidad} unidades")
        print(f"PRECIO: s/. {p.precio:.2f}")
        print("="*30)

#D 

class SistemaInventario:
    def __init__(self, Inventario):
        self.inventario = Inventario  

    def ejecutar(self):
        while True:
            print("\n--- CONTROL DE INVENTARIO - Minimarket UNAP ---")
            print("1. Registrar | 2. Entrada | 3. Salida | 4. Reporte | 5. Escáner | 6. Salir")
            opcion = input("Seleccione opción: ")

            try:
                if opcion == "1":
                    p = Producto(int(input("ID: ")), input("Nombre: "), 
                                 int(input("Stock: ")), float(input("Precio: ")))
                    self.inventario.guardar(p)
                    print("Operación exitosa.")
                
                elif opcion in ["2", "3"]:
                    id_p = int(input("ID: "))
                    cant = int(input("Cantidad: "))
                    self.inventario.actualizar(id_p, cant if opcion == "2" else -cant)
                    print("Stock actualizado.")
                
                elif opcion == "4":
                    datos = self.inventario.obtener_lista()
                    GeneradorReportes.imprimir_tabla(datos)
                    GeneradorReportes.imprimir_resumen(datos)
                
                elif opcion == "5":  
                    id_p = int(input("Escanee código (ingrese ID): "))
                    producto_leido = self.inventario.buscar_por_id(id_p)
                    GeneradorReportes.mostrar_detalle_escaneo(producto_leido)

                elif opcion == "6":
                    break
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    memoria = InventarioEnMemoria()
    app = SistemaInventario(memoria)
    app.ejecutar()