#validaciones 
from Tiempo import Tiempo
from Validar import validar_tipo,es_positivo,no_es_vacio
from enum import Enum 

def nombre_valido(nombre:str):
    n = ""
    if(validar_tipo(nombre,str) and no_es_vacio(nombre)):
        n = nombre
    else:
        raise Exception("Nombre no es valido")
    return n

def artista_valido(artista:str):
    a = ""
    if(validar_tipo(artista,str) and no_es_vacio(artista)):
        a = artista
    else:
        raise Exception("El artista no es valido")
    return a
    
# def genero_valido(genero:Enum):
#     g = None
#     if(validar_tipo(genero,Enum)) and no_es_vacio:
#         g = genero
#     else:
#         raise Exception("Genero no valido")
#     return g

def likes_valido(likes:int):
    l = 0
    if validar_tipo(likes,int) and no_es_vacio(likes) and es_positivo(likes) :
        l = likes
    else:
        raise Exception("Cantidad de likes no validos")
    return l

# clase
class Cancion:
    def __init__(self , nombre : str , artista : str , duracion : Tiempo , genero : Enum , likes : int) -> None:
        self.__nombre = nombre_valido(nombre)
        self.__artista = artista_valido(artista)
        self.__duracion = duracion
        self.__genero =  genero
        self.__likes = likes_valido(likes)
        
        
    def __repr__(self) -> str:
        return f'{self.__nombre} - {self.__artista} ({self.__duracion})'

    
    def duracion(self)-> Tiempo :
        return self.__duracion
    
    def likes(self)-> int:
        return self.__likes
    
    def mayor_duracion(cancion_uno,cancion_dos):
        return Tiempo.es_mayor(cancion_uno.duracion(),cancion_dos.duracion())
    
    
    def agregar_likes(self,likes:int):
        if validar_tipo(likes,int) and es_positivo(likes):
            self.__likes = self.__likes + likes
        else:
            raise Exception("El valor de likes no es valida")

    def mas_votado(cancio_uno,cancion_dos):
        cancion_con_mas_likes = None
        
        if cancio_uno.mismo_artista(cancion_dos) and cancio_uno.mismo_genero(cancion_dos):
            cancion_con_mas_likes = cancio_uno.mayor_cantidad_likes(cancion_dos)
        else:
            raise Exception("Alguno de los dos valores no cumplen con la condición")
        
        return cancion_con_mas_likes
        
    def mismo_artista(cancion_uno,cancion_dos)-> bool:
        return cancion_uno.__artista == cancion_dos.__artista
    
    def mismo_genero(cancion_uno,cancion_dos)-> bool:
        return cancion_uno.__genero == cancion_dos.__genero
    
    
    #Mas likes
    def mayor_cantidad_likes(cancion_uno,cancion_dos):
        return cancion_uno if cancion_uno.__likes > cancion_dos.__likes else cancion_dos
    
class Genero(Enum):
    ROCK = 1
    JAZZ = 2
    BLUES = 3
    FUNK = 4
    REGGAE = 5
    RAP = 6
