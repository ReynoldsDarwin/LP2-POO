class Person:
    def __init__(self,nombre):
        self.nombre = nombre

    def saludad(self):
        print(f"Hola, soy {self.nombre}")

persona1 = Person("Carlos")
persona2 = Person("Maria")
persona1.saludad()
persona2.saludad()