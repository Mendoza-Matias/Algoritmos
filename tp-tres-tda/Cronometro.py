from Tiempo import Tiempo
#validaciones



#clases
class Cronometro:
    def __init__(self , t1 : Tiempo , t2 : Tiempo) -> None:
        self.__tiempo_inicial = t1
        self.__tiempo_final = t2
    
    def __repr__(self) -> str:
        return f'T1 : {self.__tiempo_inicial} | T2 : {self.__tiempo_final}'
    
    def comenzar(self,h:int , m: int , s:int):
        self.__tiempo_inicial = Tiempo(h,m,s) #Le seteo a tiempo inicial un objeto de tipo tiempo
        
    def finalizar(self, h:int , m:int , s:int):
        self.__tiempo_final = Tiempo(h,m,s)
        
    def tiempo_empleado(self):
        return self.__tiempo_inicial - self.__tiempo_final
        