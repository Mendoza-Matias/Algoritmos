class Propiedad:
    def __init__(self,calle:str,numero:int , localidad:str , anio_de_construccion:int , cantidad_de_ambientes:int):
        self.__calle = calle
        self.__numero = numero
        self.__localidad = localidad,
        self.__anio_de_construccion = anio_superior_1870(anio_de_construccion)
        self.__cantidad_de_ambientes = cantidad_de_ambientes
    

    def __repr__(self) -> str:
        return f' Calle : {self.__calle} \n Numero : {self.__numero} \n Localidad : {self.__localidad}'
    
    def misma_localidad(self,other_object)-> bool:
        return self.__localidad == other_object.__localidad
    
    def misma_calle(self,other_objetc) -> bool:
        return self.calle == other_objetc.__calle
    
    def mayor_numeracion(self,other_object)-> int:
        propiedad_mayor = None
        
        if self.misma_calle(other_object):
            propiedad_mayor = self.propiedad_con_mayor_numeracion(other_object)
        else:
            raise Exception("Las propiedades se encuentran en calles diferentes")        
        return propiedad_mayor
        
    def propiedad_con_mayor_numeracion (self,other_objet)-> int:
        return self.__numero if self.__numero > other_objet.__numero else other_objet.__numero
    
    def impuestos_arba(self)-> str:
        impuesto = ""
        if self.es_de_anio_mayor_1850_menor_1950:
            impuesto = self.impuestos_por_ambientes()
        else :
            impuesto = self.impuesto_propiedad_mayor_1950()
             
        return impuesto
    
    def es_de_anio_mayor_1850_menor_1950(self)-> bool:
        return self.__anio_de_construccion > 1870 and self.__anio_de_construccion < 1949
    
    def impuestos_por_ambientes(self)-> str:
        impuesto = ""
        if self.es_de_cantidad_ambientes(1,3):
            impuesto = "5%"
        elif self.es_de_cantidad_ambientes(4,6):
            impuesto = "10%"
        else:
            impuesto = "25%"
        return impuesto     
    
    def impuesto_propiedad_mayor_1950(self)-> str:
        impuestos = ""
        if self.es_de_cantidad_ambientes(1,5):
            impuestos = "5%"
        else : 
            impuestos = "35%"
        return impuestos
    
    def es_de_cantidad_ambientes (self,amb_uno:int,amb_dos:int)-> bool:
        return self.__cantidad_de_ambientes > amb_uno and self.__cantidad_de_ambientes < amb_dos
    
    #Calcula los impuestos de una propiedad con año de constucción mayor a 1950
    
    
#Validaciones ---

def anio_superior_1870(anio_construccion:int)-> int:
        if anio_construccion >= 1870:
            anio = anio_construccion
        else :
            raise Exception("El año de construcción debe ser superior o igual a 1870")
        return anio