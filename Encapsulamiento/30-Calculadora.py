class Calculadora:
    def _init_(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def get_num1(self):
        return self.__num1
    def get_num2(self):
        return self.__num2

    def set_num1(self, nuevo_num1):
        self.__num1 = nuevo_num1
    def set_num2(self, nuevo_num2):
        self.__num2 = nuevo_num2

    def sumar(self):
        return self._num1 + self._num2
    
    def restar(self):
        return self._num1 - self._num2
    
    def multiplicar(self):
        return self._num1 * self._num2
    
    def dividir(self):
        if self.__num2 != 0:
            return self._num1 / self._num2
        else:
            return "Error: No se puede dividir entre 0"

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

calc = Calculadora(num1, num2)

print("\nResultados de las operaciones:")
print(f"Suma: {calc.sumar()}")
print(f"Resta: {calc.restar()}")
print(f"Multiplicación: {calc.multiplicar()}")
print(f"División: {calc.dividir()}")