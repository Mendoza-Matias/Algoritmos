from Validar import validar_tipo,es_positivo

#validar horas
def validar_horas(horas:int)-> int:
    h = 0
    if validar_tipo(horas,int) and es_positivo(horas):
        h = horas    
    else:
        raise Exception("Horas no validos")
    return h

#validar minutos
def validar_minutos(minutos:int) -> int:
    m = 0
    if validar_tipo(minutos,int) and es_positivo(minutos):
        m = minutos
    else:
        raise Exception("Minutos no validos")
    return m

#validar segundos
def validar_segundos(segundos:int) -> int:
    s = 0
    if validar_tipo(segundos,int) and es_positivo(segundos) and segundos < 59:
        s = segundos
    else:
        raise Exception("Segundo no validos")
    return s

#Clase
class Tiempo :
    def __init__(self , horas: int , minutos : int , segundos : int):
        self.__horas =  validar_horas(horas)
        self.__minutos = validar_minutos(minutos)
        self.__segundos = validar_segundos(segundos)
        
    def __repr__(self) -> str:
        return f'{self.__horas}:{self.__minutos}:{self.__segundos}'
    
    #Me devuelve la diferencia y me retorna un nuevo objeto
    def __sub__(tiempo_uno,tiempo_dos):
        diferencia_en_segundos = abs(tiempo_uno.tiempo_a_segundos() - tiempo_dos.tiempo_a_segundos())
        return Tiempo.desde_segundos(diferencia_en_segundos)
    
    def tiempo_a_segundos(self) -> int:
        return self.__horas * 3600 + self.__minutos * 60 + self.__segundos
    
    def desde_segundos(segundos:int) -> 'Tiempo' :
        return Tiempo(segundos // 3600 , (segundos % 3600) // 60 , (segundos % 3600) % 60)
    
    # ---
    
    def es_mayor(tiempo_uno,tiempo_dos):
      
      total_s_uno = tiempo_uno.tiempo_a_segundos()
      total_s_dos = tiempo_dos.tiempo_a_segundos()
      
      mas_grande = Tiempo.tiempo_en_segundos_mayor(total_s_uno,total_s_dos)
      
      return Tiempo.desde_segundos(mas_grande)

    def tiempo_en_segundos_mayor(segundos_uno,segundos_dos):
        return segundos_uno if segundos_uno > segundos_dos else segundos_dos
    