class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f'El libro "{self.titulo}" ha sido prestado.')
        else:
            print(f'El libro "{self.titulo}" no está disponible actualmente.')

    def devolver(self):
        self.disponible = True
        print(f'El libro "{self.titulo}" ha sido devuelto.')


class Prestamo:
    def __init__(self, libro, fecha_prestamo):
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.devuelto = False

    def marcar_devolucion(self):
        self.devuelto = True
        self.libro.devolver()


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.prestamos = []

    def realizar_prestamo(self, libro, fecha):
        if libro.disponible:
            libro.prestar()
            prestamo = Prestamo(libro, fecha)
            self.prestamos.append(prestamo)
        else:
            print(f'❌ No se puede realizar el préstamo: "{libro.titulo}" no está disponible.')

    def mostrar_prestamo(self):
        print(f'\nPréstamos de {self.nombre}:')
        for p in self.prestamos:
            estado = 'Devuelto' if p.devuelto else 'Pendiente'
            print(f' - {p.libro.titulo} ({estado}) - Fecha: {p.fecha_prestamo}')


def main():
    print("📚 REGISTRO DE LIBROS")
    cantidad = int(input("¿Cuántos libros deseas registrar?: "))

    libros = []  # Lista dinámica de libros
    for i in range(cantidad):
        print(f"\n--- Libro {i + 1} ---")
        titulo = input("Título: ")
        autor = input("Autor: ")
        isbn = input("ISBN: ")
        libros.append(Libro(titulo, autor, isbn))

    print("\n👤 REGISTRO DE USUARIO")
    nombre_usuario = input("Nombre del usuario: ")
    id_usuario = input("ID del usuario: ")

    usuario1 = Usuario(nombre_usuario, id_usuario)

    print("\n📅 PRÉSTAMOS DE LIBROS")
    for i, libro in enumerate(libros):
        fecha = input(f"Fecha del préstamo de '{libro.titulo}' (YYYY-MM-DD): ")
        usuario1.realizar_prestamo(libro, fecha)
        usuario1.mostrar_prestamo()

    print("\n📘 DEVOLUCIONES")
    for i, libro in enumerate(libros):
        devolver = input(f"¿Deseas devolver '{libro.titulo}'? (s/n): ").lower()
        if devolver == "s":
            usuario1.prestamos[i].marcar_devolucion()

    usuario1.mostrar_prestamo()
    print("==========================================")
    print("Fin del programa.")


if __name__ == "__main__":
    main()
