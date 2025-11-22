import gc

class Curso:
    def __init__(self, nombre, codigo, profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        print(f"\nnombre del curso: {self.nombre}, codigo del curso: {self.codigo}, docente: {self.profesor}")

    def mostrar_informacion(self):
        print(f"Curso Registrado: {self.nombre} | cod. del Curso: {self.codigo} | Docente: {self.profesor}")

    def __del__(self):
        print(f"Curso eliminado: {self.nombre}")


cursos = []

n = int(input("¿Cuántos cursos va registrar?: "))

for i in range(n):
    print(f"\n--- Curso {i+1} ---")
    nombre = input("Nombre del curso: ")
    codigo = int(input("Codigo del curso: "))
    profesor = input("Docente del curso: ")

    curso = Curso(nombre, codigo, profesor)
    curso.mostrar_informacion()
    cursos.append(curso)

del curso
cursos.clear()
gc.collect()

print("\nFin del programa")
