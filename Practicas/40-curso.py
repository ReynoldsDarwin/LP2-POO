class Estudiante:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
        
class Curso:
    def __init__(self,nombre_curso):
        self.nombre_curso = nombre_curso
        self.lista = []
        
    def agregar_estudiante(self,estudiante):
        self.lista.append(estudiante)
        print(f"Estudiante {estudiante.nombre} agregado al curso {self.nombre_curso}")
    def mostrar_estudiantes(self):
        if not self.lista:
            print("No hay estudiantes en el curso")
        else:
            print(f"\nLista de estudiantes en el curso {self.nombre_curso}")
            for estudiante in self.lista:
                print(f"Nombre: {estudiante.nombre}, Edad: {estudiante.edad}")
curso = Curso("Matematicas")
while True:
    print("\n======= Menu de cursos ========")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Salir")

    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        nombre = input("Nombre del estudiante: ")
        edad = input("Edad del estudiante: ")
        estudiante = Estudiante(nombre,edad)
        curso.agregar_estudiante(estudiante)
    elif opcion == "2":
        curso.mostrar_estudiantes()
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion no valida, intente de nuevo")

