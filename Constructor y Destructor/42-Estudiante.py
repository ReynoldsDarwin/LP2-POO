import gc

class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        print(f"Estudiante registrado: {self.nombre}, {self.edad} años, {self.carrera}")

    def mostrar_informacion(self):
        print(f"{self.nombre} estudia {self.carrera} y tiene {self.edad} años.")

    def __del__(self):
        print(f"Estudiante eliminado: {self.nombre}")


# --- Programa principal ---
grupo = []

cantidad = int(input("¿Cuántos estudiantes quieres registrar? "))

for i in range(cantidad):
    print(f"\n--- Estudiante {i+1} ---")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    carrera = input("Carrera: ")

    estudiante = Estudiante(nombre, edad, carrera)
    estudiante.mostrar_informacion()
    grupo.append(estudiante)

# Eliminar estudiantes
grupo.clear()
gc.collect()
print("\nFin de programa")
