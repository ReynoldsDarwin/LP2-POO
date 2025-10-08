class Producto:
    def __init__(self,nombre,precio):
        self.__nombre = nombre
        self.__precio = precio

    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self,nuevo_precio):
        if nuevo_precio >= 0:
            self.__precio = nuevo_precio
        else:
            print("Error, precio menor o igual a cero.")

    def mostrar_producto(self):
        print(f"Producto: {self.__nombre} -- Precio: {self.__precio}.")

def main():
    producto = Producto("Laptop",2500)
    producto.mostrar_producto()
    producto.precio = 3000
    producto.mostrar_producto()
    producto.precio = -50

if __name__ == "__main__":
    main()

        
