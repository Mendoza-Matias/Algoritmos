from Validar import validar_tipo
 
class Tiempo:
    def __init__(self,horas:int,minutos:int,segundo:int):
        self.__horas = validar_horas(horas)
        self.__minutos = validar_minutos(minutos)
        self.__segundos = validar_segundo(segundo)
        
    
    def __repr__(self) -> str:
        return f' Horas : {self.__horas} \n Minutos : {self.__minutos} \n Segundos : {self.__segundos}'
    
    def get_horas(self) -> int:
        return self.__horas
    
    def get_minutos(self) -> int:
        return self.__minutos
    
    def get_segundos(self) -> int:
        return self.__segundos
    
    def tiempo_a_segundo(self)-> str:
        return f'{self.__horas * 3600} {self.__minutos * 60} {self.__segundos}'
    
    def tiempo_desde_segundos(self)->str:
        return f'{self.__horas // 3600} {self.__minutos // 60} {self.__segundos}'
    
    def mayor_duracion(self,other:object)-> str:
        tiem_ = ""
        if self.__horas > other.__horas :
            tiem_ = str(self)
        else:
            tiem_ = str(other)
            
        return tiem_
           

#Validaciones 

def validar_horas(horas:int)-> int:
    hora_ = 0
    if validar_tipo(horas,int):
        hora_ = horas
    else:
        raise Exception("Valor de Hora invalido")   
    return hora_
    
def validar_minutos(minutos:int) -> int:
    min_ = 0
    if validar_tipo(minutos,int) and minutos > 0 and minutos <= 59:
        min_ = minutos
    else:
        raise Exception("Valor de Minutos invalido")
    return min_
        
def validar_segundo(segundo:int)-> int :
    seg_ = 0
    if validar_tipo(segundo,int) and segundo > 0 and segundo <= 59:
        seg_ = segundo
    else:
        raise Exception("Valor de Segundos invalido")
    return seg_