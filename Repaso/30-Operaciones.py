class Operaciones:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def sumar(self,a,b,c=None):
        if c is not None:
            return self.a + self.b + self.c
        else:
            return self.a + self.b

oper1 = Operaciones(1, 2, 3)

print("oper1 suma a+b:", oper1.sumar(oper1.a, oper1.b))
print("oper1 suma a+b+c:", oper1.sumar(oper1.a, oper1.b, oper1.c))

