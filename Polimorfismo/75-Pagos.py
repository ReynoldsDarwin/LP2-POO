class MetodoPago:
    def pago(self):
        pass
    
class TargetaDeCredito(MetodoPago):
    def __init__(self):
        self.nombre = "Tarjeta de Crédito"
    def pago(self):
        return f"Pago realizado con {self.nombre}"
class PayPal(MetodoPago):
    def __init__(self):
        self.nombre = "PayPal"
    def pago(self):
        return f"Pago realizado con {self.nombre}"

class PagoEfectivo(MetodoPago):
    def __init__(self):
        self.nombre = "Efectivo"
    def pago(self):
        return f"Pago realizado con {self.nombre}"
    
class Yape(MetodoPago):
    def __init__(self):
        self.nombre = "Yape"
    def pago(self):
        return f"Pago realizado con {self.nombre}"
    
metodos_pago = [TargetaDeCredito(), PayPal(), PagoEfectivo(), Yape()]
for metodo in metodos_pago:
    print(metodo.pago())