class Persona:
    def __init__(self, nombre, dia, mes):
        self.nombre = nombre
        self.dia = dia
        self.mes = mes

    def signo_zodiacal(self):
        signos = [
            ("Capricornio", (12, 22), (1, 19)),
            ("Acuario", (1, 20), (2, 18)),
            ("Piscis", (2, 19), (3, 20)),
            ("Aries", (3, 21), (4, 19)),
            ("Tauro", (4, 20), (5, 20)),
            ("Géminis", (5, 21), (6, 20)),
            ("Cáncer", (6, 21), (7, 22)),
            ("Leo", (7, 23), (8, 22)),
            ("Virgo", (8, 23), (9, 22)),
            ("Libra", (9, 23), (10, 22)),
            ("Escorpio", (10, 23), (11, 21)),
            ("Sagitario", (11, 22), (12, 21)),
        ]
        for signo, inicio, fin in signos:
            if (self.mes == inicio[0] and self.dia >= inicio[1]) or (self.mes == fin[0] and self.dia <= fin[1]):
                return signo
        return "Desconocido"

nombre = input("Ingresa tu nombre: ")
dia = int(input("Ingresa tu día de nacimiento (1-31): "))

meses_dict = {
    "Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4,
    "Mayo": 5, "Junio": 6, "Julio": 7, "Agosto": 8,
    "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12
}

mes_nombre = input("Ingresa tu mes de nacimiento (ejemplo: Marzo): ")
mes = meses_dict.get(mes_nombre.capitalize(), 0)

if mes == 0 or dia < 1 or dia > 31:
    print("⚠️ Ingresa una fecha válida")
else:
    persona = Persona(nombre, dia, mes)
    signo = persona.signo_zodiacal()
    print(f"Hola {persona.nombre}, naciste el {dia} de {mes_nombre} y tu signo zodiacal es: {signo}.")
