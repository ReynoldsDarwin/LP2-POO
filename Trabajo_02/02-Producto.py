class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio
    
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, valor):
        if valor < 0:
            print("Error: El precio no puede ser negativo")
        else:
            self.__precio = valor
    
    def aplicar_descuento(self, porcentaje):
        if porcentaje < 0 or porcentaje > 100:
            print("Error: El porcentaje debe estar entre 0 y 100")
        else:
            descuento = self.__precio * (porcentaje / 100)
            self.__precio -= descuento
            print(f"Descuento aplicado. Nuevo precio: ${self.__precio:.2f}")
    
    def mostrar_info(self):
        print(f"Producto: {self.__nombre} - Precio: ${self.__precio:.2f}")
def main():
    producto1 = Producto("Laptop", 1000)
    producto2 = Producto("Mouse", 25)
    
    producto1.mostrar_info()
    producto2.mostrar_info()

    producto1.aplicar_descuento(150)
    producto1.aplicar_descuento(-10)

    producto2.precio = -50
    producto2.mostrar_info()

    producto2.precio = 30
    producto2.mostrar_info()

if __name__ == "__main__":
    main()