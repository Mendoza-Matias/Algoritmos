from Validar import validar_tipo
 
class Tiempo:
    def __init__(self,horas:int,minutos:int,segundo:int):
        self.__horas = self.validar_horas(horas)
        self.__minutos = self.validar_minutos(minutos)
        self.__segundos = self.validar_segundo(segundo)
        
        
    def validar_horas(self,horas:int)-> int:
        hora_ = 0
        if validar_tipo(horas,int) and horas > 0 and horas <= 23:
            hora_ = horas
        else:
            raise Exception("Valor de Hora invalido")   
        return hora_
    
    def validar_minutos(self,minutos:int) -> int:
        min_ = 0
        if validar_tipo(minutos,int) and minutos > 0 and minutos <= 59:
            min_ = minutos
        else:
            raise Exception("Valor de Minutos invalido")
        
    def validar_segundo(self,segundo:int)-> int :
        seg_ = 0
        if validar_tipo(segundo,int) and segundo > 0 and segundo <= 59:
            seg_ = segundo
        else:
            raise Exception("Valor de Segundos invalido")
        return seg_