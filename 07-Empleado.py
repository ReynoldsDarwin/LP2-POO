class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo =  cargo
        self.salario = salario
        
    def aplicarAumento(self):
        if self.cargo.lower() == "gerente":
            self.salario *= 1.10
            
        elif self.cargo.lower() == "supervisor":
            self.salario *= 1.07
        
        elif self.cargo.lower() == "operario":
            self.salario *= 1.05
        
        elif self.cargo.lower() == "interno":
            self.salario *= 1.00
            
        return f"{self.nombre} es {self.cargo} y ahora ganará un total de: {self.salario} nuevos soles."
    
nombre = input("Ingrese el nombre: ")
cargo = input("Ingrese el cargo(gerente/supervisor/operario/interno): ")
salario = float(input("Ingrese su salario actual: "))

empleado = Empleado(nombre,cargo,salario)
print(empleado.aplicarAumento())
            
        
        
