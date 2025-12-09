class Division:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def dividir(self):
        try:
            resultado = self.a / self.b
            return resultado
        except ZeroDivisionError:
            return "Error: No se puede dividir entre cero"
        except Exception as e:
            return f"Ocurrio un error: {e}"
        finally:
            print("Operacion finalizada")
            
operacion = Division(10,0)
print(operacion.dividir())