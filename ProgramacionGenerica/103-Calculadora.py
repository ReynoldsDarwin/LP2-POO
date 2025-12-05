from typing import TypeVar, Generic

T = TypeVar('T', int, float)

class Calculadora(Generic[T]):
    def __init__(self,a:T,b:T):
        try:
            self.a = a
            self.b = b
        except Exception as e:
            raise TypeError(f"Error al asignar valores: {e}")
        
    def sumar(self)->T:
        try:
            return self.a + self.b
        except Exception as e:
            raise TypeError(f"Error al sumar: {e}")
    
    def restar(self)->T:
        try:
            return self.a - self.b
        except Exception as e:
            raise TypeError(f"Error al restar: {e}")
    
    def multiplicar(self)->T:
        try:
            return self.a * self.b
        except Exception as e:
            raise TypeError(f"Error al multiplicar: {e}")
    
    def dividir(self)->T:
        try:
            if self.b == 0:
                raise ZeroDivisionError ("No se puede dividir entre cero.")
            return self.a / self.b
        except Exception as e:
            raise ArithmeticError(f"Error al dividir: {e}")
    
def main():
    try:
        calc_int = Calculadora[int](10,5)
        print("Suma:", calc_int.sumar())
        print("Resta:", calc_int.restar())
        print("Multiplicacion:", calc_int.multiplicar())
        print("division:", calc_int.dividir())
        
        calc_float = Calculadora[float](10.5,2.5)
        print("Suma_f:", calc_float.sumar())
        print("Resta_f:", calc_float.restar())
        print("Multiplicacion_f:", calc_float.multiplicar())
        print("division_f:", calc_float.dividir())
    except Exception as error:
        print(f"Ocurrió un error: {error}")
         
# def main():
#     dato_1 = float(input("Ingrese el primer numero a operar: "))
#     dato_2 = float(input("Ingrese el segundo numero a operar: "))
    
#     calculadora = Calculadora(dato_1,dato_2)
    
#     print(f"La suma es: {calculadora.sumar()}")
#     print(f"La resta es: {calculadora.restar()}")
#     print(f"La multiplicacion es: {calculadora.multiplicar()}")
#     print(f"La division es {calculadora.dividir()}")
    
    
if __name__ == "__main__":
    main()
    