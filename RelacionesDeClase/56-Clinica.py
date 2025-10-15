class Paciente:
    def __init__(self,nombre,dni):
        self.nombre =  nombre
        self.dni = dni

class Cita:
    def __init__(self,paciente,fecha,especialidad):
        self.paciente = paciente
        self.fecha = fecha
        self.especialidad = especialidad

    def mostrar_informacion(self):
        print(f"Paciente: {self.paciente.nombre} DNI: {self.paciente.dni} Fecha {self.fecha} Especialidad: {self.especialidad}")
        

class Consultorio:
    def __init__(self):
        self.citas = []
    def agendar_citas(self,nombre,dni,fecha,especialidad):
        paciente = Paciente(nombre,dni)
        cita = Cita(paciente,fecha,especialidad)
        self.citas.append(cita)
        print("Cita agendada correctamente")
    def mostrar_citas(self):
        if not self.citas:
            print("No hay citas agendadas")
        else:
            print("\nLista de citas agendadas")
            for cita in self.citas:
                cita.mostrar_informacion()
    def calcelar_citas(self,dni,fecha):
        for cita in self.citas:
            if cita.paciente.dni==cita.fecha==fecha:
                self.citas.remove(cita)
                print(f"cita del paciente {cita.paciente.nombre} cancelado")
                return
            print("Cita no encontraba")
consultorio = Consultorio()

while True:
    print("\n======= Menu de consultorio ========")
    print("1. Agendar Cita")
    print("2. Mostrar todas las citas")
    print("3. Cancelar cita")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        nombre = input("Nombre del paciente: ")
        dni = input("DNI del paciente: ")
        fecha = input("Fecha de la cita (DD/MM/AAAA)")
        especialidad = input("Especialidad médica: ")
        consultorio.agendar_citas(nombre,dni,fecha,especialidad)
    elif opcion == "2":
        consultorio.mostrar_citas()
    elif opcion == "3":
        dni = input("DNI del paciente: ")
        fecha = input("Fecha de la cita a cancelar (DD/MM/AAAA): ")
        consultorio.calcelar_citas(dni,fecha)
    elif opcion == "4":
        print("=======================================")
        print("Saliendo del sistema de citas medicas...\n ")
        break
    else:
        print("Opcion no válida.")



    
