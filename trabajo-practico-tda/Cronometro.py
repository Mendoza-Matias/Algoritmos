from Tiempo import Tiempo

class Cronometro:
    def __init__(self,horas:int,minutos:int,segundos:int) -> None:
        self.__horas = Tiempo.validar_horas(horas)
        self.__minutos = Tiempo.validar_minutos(minutos) 
        self.__segundos = Tiempo.validar_segundo(segundos)
    
    
    def __repr__(self) -> str:
        return Tiempo.__repr__
    
    def tiempo_inicial(horas:int,minutos:int,segundos:int) -> Tiempo:
        tiempo = Tiempo(horas,minutos,segundos)
        return tiempo
    
    
    def tiempo_final(horas:int,minutos:int,segundos:int) -> Tiempo:
        tiempo = Tiempo(horas,minutos,segundos)
        return tiempo
    
    def diferencia_de_tiempo(tiempo_inicial:Tiempo,tiempo_final:Tiempo) -> Tiempo :
        dif_horas = (tiempo_final.get_horas() - tiempo_inicial.get_horas())
        dif_minutos = (tiempo_final.get_minutos() - tiempo_inicial.get_minutos())
        dif_seg = (tiempo_final.get_segundos() - tiempo_inicial.get_segundos())
        
        tiempo = Tiempo(dif_horas,dif_minutos,dif_seg)
        return tiempo