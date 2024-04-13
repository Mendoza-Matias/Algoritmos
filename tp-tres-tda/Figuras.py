#Validaciones
from Validar import validar_tipo

def validar_lado(lado:float):
    l= 0
    if validar_tipo(lado,float):
        l = lado
    else:
        raise Exception("El lado ingresado no es valido")
    return l

#Clases
class Rectangulo:
    def __init__(self, lado_uno :float , lado_dos :float) -> None:
        self.__lado_uno = validar_lado(lado_uno)
        self.__lado_dos = validar_lado(lado_dos)
        
    def area(self):
        return self.__lado_uno * self.__lado_dos
    
    def perimetro(self):
        return 2 * (self.__lado_uno +  self.__lado_dos)
    

class Cuadrado:
    def __init__(self,lado:float) -> None:
        self.__forma = Rectangulo(lado,lado) #Creo una instancia de un objeto con los lados iguales y asi acceso a sus metodos
    
    def area(self):
        return self.__forma.area()    
        
    def perimetro(self):
        return self.__forma.perimetro()
        