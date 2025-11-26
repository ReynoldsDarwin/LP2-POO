class Empleado:
    nombre: str
    salario: float

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_pago(self) -> float:
        raise NotImplementedError

class EmpleadoTiempoCompleto(Empleado):
    def calcular_pago(self) -> float:
        return self.salario

class EmpleadoPorHoras(Empleado):
    horas_trabajadas: float

    def __init__(self, nombre, salario_por_hora, horas_trabajadas):
        super().__init__(nombre, salario_por_hora)
        self.horas_trabajadas = horas_trabajadas

    def calcular_pago(self) -> float:
        return self.salario * self.horas_trabajadas

def main():
    empleados = [
        EmpleadoTiempoCompleto("Miguel Quispe", 3500.00),
        EmpleadoPorHoras("Rocio Apaza", 25.50, 40.0),
        EmpleadoTiempoCompleto("Fernanda Lopez", 4200.00),
        EmpleadoPorHoras("Juan Contreras", 15.75, 20.0)
    ]

    for empleado in empleados:
        pago = empleado.calcular_pago()
        print(f"Empleado: {empleado.nombre} | Pago calculado: ${pago:.2f}")

if __name__ == "__main__":
    main()