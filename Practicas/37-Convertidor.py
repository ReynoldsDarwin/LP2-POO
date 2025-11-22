class Temperatura:
    def __init__(self, valor=0):
        self.__valor = valor  

    def get_valor(self):
        return self.__valor

    def set_valor(self, nuevo_valor):
        self.__valor = nuevo_valor

    def fahrenheit_a_celsius(self):
        return (self.__valor - 32) * 5/9

    def celsius_a_fahrenheit(self):
        return (self.__valor * 9/5) + 32

temperatur = Temperatura()

temperatur.set_valor(98.6)
print(f"{temperatur.get_valor()}°F = {temperatur.fahrenheit_a_celsius()}°C")

temperatur.set_valor(10)
print(f"{temperatur.get_valor()}°C = {temperatur.celsius_a_fahrenheit()}°F")
