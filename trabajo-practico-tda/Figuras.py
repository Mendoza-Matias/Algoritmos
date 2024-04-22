class Rectangulo:
    def __init__(self,lado_uno:float,lado_dos:float):
        self.__lado_uno = lado_uno
        self.__lado_dos = lado_dos
        
    def __repr__(self) -> str:
        return f'{self.__lado_uno} {self.__lado_dos}'
    
    
    
class Cuadrado:
    def __init__(self,lado:float) -> None:
        self.__forma = Rectangulo(lado,lado)
        
        
    def area(self):
        return self.__forma
    
    def perimetro(self):
        return self.__forma