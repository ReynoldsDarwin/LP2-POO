class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius
        print("Objeto temperatura creado")

    def a_fahrenheit(self):
        fahrenheit = (self.celsius * 9/5) + 32
        return fahrenheit
    
temperatura_celcius = float(input("Ingrese la temperatura en grados Celsius: "))
temperatura = Temperatura(temperatura_celcius)
print(f"{temperatura.celsius}°C son {temperatura.a_fahrenheit()}°F")

del temperatura

try:
    temperatura.a_fahrenheit()

except NameError:
    print("Objeto Temperatura destruido")
