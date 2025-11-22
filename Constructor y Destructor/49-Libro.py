import gc

class Libro:
    def __init__(self,titulo,autor,anio):
        self.titulo = titulo
        self.autor = autor
        self.anio  = anio

    def mostrar_informacion(self):
        print(f"Libro registrado {self.titulo} de {self.autor} {self.anio}")

    def __del__(self):
        print(f"Libro eliminado {self.titulo}")

biblioteca = []

cantidad = int(input("Cuantos libros desea registrar?: "))
for i in range  (cantidad):
    print(f"\n--- Libro {i+1} ---")
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    anio = int(input("Año de publicacion: "))

    libro = Libro(titulo,autor,anio)
    libro.mostrar_informacion()
    biblioteca.append(libro)

biblioteca.clear()
del libro
gc.collect()
print("Fin del programa")
