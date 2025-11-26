class ConversorTemperatura:
    fahrenheit: float

    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit

    @staticmethod
    def celsius_a_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @classmethod
    def desde_celsius(cls, celsius):
        fahrenheit = cls.celsius_a_fahrenheit(celsius)
        return cls(fahrenheit)

def main():
    calculo_rapido = ConversorTemperatura.celsius_a_fahrenheit(100)
    print(f"Cálculo estático (100°C): {calculo_rapido}°F")

    clima_hoy = ConversorTemperatura.desde_celsius(25)
    print(f"Objeto creado desde Celsius (25°C): {clima_hoy.fahrenheit}°F")

    horno = ConversorTemperatura(350)
    print(f"Objeto creado directo (350°F): {horno.fahrenheit}°F")

if __name__ == "__main__":
    main()