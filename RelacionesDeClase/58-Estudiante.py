class Estudiante:
    def __init__(self, nombre, dni, codigo_estudiante):
        self.nombre = nombre
        self.dni = dni
        self.codigo_estudiante = codigo_estudiante
        self.cursos = []

    def inscribirse(self, curso):  
        self.cursos.append(curso)  
        curso.agregar_estudiante(self)

    def mostrar_informacion(self):
        print(f"\nEstudiante: {self.nombre} | DNI: {self.dni} | Código: {self.codigo_estudiante}")
        print("Cursos inscritos:")
        for curso in self.cursos:
            print(f" - {curso.nombre_curso}")


class Profesor:
    def __init__(self, nombre, dni, especialidad):
        self.nombre = nombre
        self.dni = dni
        self.especialidad = especialidad

    def mostrar_informacion(self):
        print(f"Profesor: {self.nombre} | DNI: {self.dni} | Especialidad: {self.especialidad}")


class Curso:
    def __init__(self, nombre_curso, profesor):
        self.nombre_curso = nombre_curso
        self.profesor = profesor
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        if estudiante not in self.estudiantes:
            self.estudiantes.append(estudiante)

    def mostrar_detalles(self):
        print(f"\nCurso: {self.nombre_curso}")
        print("Profesor:")
        self.profesor.mostrar_informacion()
        print("Estudiantes inscritos:")
        for est in self.estudiantes:
            print(f" - {est.nombre} ({est.codigo_estudiante})")


class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = []

    def agregar_curso(self, curso):  
        self.cursos.append(curso)

    def mostrar_cursos(self): 
        print(f"\nUniversidad: {self.nombre}")
        for curso in self.cursos:
            curso.mostrar_detalles()

profe1 = Profesor("Ing. Juan Carlos", "01323043", "Programación")
profe2 = Profesor("Ing. Sideral Carreon", "01231233", "Nutricion Robotica")

curso1 = Curso("Lenguaje de Programación II", profe1)
curso2 = Curso("Estructura de Datos", profe1)
curso3 = Curso("Muestreo", profe2)
curso4 = Curso("Calculo Integral",profe2)
curso5 = Curso("Distribucion de Probabilidades", profe2)
curso6 = Curso("Programacion Numerica", profe2)

est1 = Estudiante("Milena Kely", "013123456", "2025007")
est2 = Estudiante("Henry Quispe Ramos", "98765432", "2025078")

univ = Universidad("Universidad Nacional del Altiplano")
univ.agregar_curso(curso1)
univ.agregar_curso(curso2)
univ.agregar_curso(curso3)
univ.agregar_curso(curso4)
univ.agregar_curso(curso4)
univ.agregar_curso(curso5)
univ.agregar_curso(curso6)



est1.inscribirse(curso1)
est1.inscribirse(curso2)
est1.inscribirse(curso3)
est2.inscribirse(curso2)
est2.inscribirse(curso3)
est2.inscribirse(curso4)
est2.inscribirse(curso5)
est2.inscribirse(curso6)

univ.mostrar_cursos()
est1.mostrar_informacion()
est2.mostrar_informacion()
est2.mostrar_informacion()
