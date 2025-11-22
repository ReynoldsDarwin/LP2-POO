class Profesor:
    def __init__(self,nombre):
        self.nombre = nombre
        
class Curso:
    def __init__(self,nombre, profesor):
        self.nombre = nombre    
        self.profesor = profesor

prof = Profesor("Dr. Morillos")
curso = Curso("Muestreo", prof)

print(curso.profesor.nombre)