class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agragaR_tarea(self,tarea):
        self.tareas.append(tarea)
        print("tarea agreagada")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas.")

        else:
            print("Tareas pendientes: ")

        for i, tarea in enumerate(self.tareas,1):
            print(f"{i} {tarea}")

mi_gestor = GestorTareas()

while True:
    print("\n---------MENU--------")
    print("1. Agregar tareas")
    print("2. Mostrar tareas: ")
    print("3. Salir.")
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        tarea = input("Escribe la tarea: ")
        mi_gestor.agragaR_tarea(tarea)
    elif opcion == "2":
        mi_gestor.mostrar_tareas()
    elif opcion == "3":
        print("-----Saliendo del gestor de tareas-----")
        break
    else:
        print("Opcion no valida. Intente de nuevo.")



