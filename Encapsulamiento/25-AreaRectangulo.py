class Rectangulo:
    def __init__(self,base,altura):
        self.__base = base
        self.__altura = altura

    def get_base(self):
        return self.__base
    def get_altura(self):
        return self.__altura
    
    def set_base(self,nueva_base):
        if nueva_base > 0:
            self.__base = nueva_base
        else: 
            print("Base no valida")

    def set_altura(self,nueva_altura):
        if nueva_altura > 0:
            self.__base = nueva_altura
        else: 
            print("Altura no valida")

    def calcular_area(self):
        return self.__base * self.__altura
    
rectangulo = Rectangulo(3,4)
print(rectangulo.calcular_area())

