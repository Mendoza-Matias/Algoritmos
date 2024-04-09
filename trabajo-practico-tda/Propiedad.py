class Propiedad:
    def __init__(self,calle:str,numero:int , localidad:str , anio_de_construccion:int , cantidad_de_ambientes:int):
        self.__calle = calle
        self.__numero = numero
        self.__localidad = localidad,
        self.__anio_de_construccion = self.validar_anio(anio_de_construccion)
        self.__cantidad_de_ambientes = cantidad_de_ambientes
    
    
    def validar_anio(self,anio_construccion:int)-> int:
        anio = 0
        if anio_construccion >= 1870:
            anio = anio_construccion
        else :
            raise Exception("El año de construcción debe ser superior o igual a 1870")
        
        return anio
    
    def __repr__(self) -> str:
        return f' Calle : {self.__calle} \n Numero : {self.__numero} \n Localidad : {self.__localidad}'
    
    def misma_localidad(self,other_object)-> bool:
        return self.__localidad == other_object.__localidad

    
    def mayor_numeracion(self,other_object)-> int:
        numeracion = 0
        if self.__calle == other_object.__calle :
            numeracion = self.propiedad_con_mayor_numeracion(other_object)
        else:
            raise Exception("Las propiedades se encuentran en calles diferentes")        
        
        return numeracion
        
    def propiedad_con_mayor_numeracion (self,other_objet)-> int:
        return self.__numero if self.__numero > other_objet.__numero else other_objet.__numero
    
    def calcular_impuestos_arba(self)-> str:
        impuesto = ""
        if self.__anio_de_construccion > 1870 and self.__anio_de_construccion < 1949:
            impuesto = self.impuestos_por_ambientes()
        else :
            impuesto = self.impuestos_mayores_1950() 
            
        return impuesto
    
    def impuestos_por_ambientes(self)-> str:
        impuesto = ""
        if self.__cantidad_de_ambientes > 1 and self.__cantidad_de_ambientes < 3 :
            impuesto = "5%"
        elif self.__cantidad_de_ambientes > 4 and self.__cantidad_de_ambientes < 6 :
            impuesto = "10%"
        else:
            impuesto = "25%"
            
        return impuesto     
    
    
    #Calcula los impuestos de una propiedad con año de constucción mayor a 1950
    def impuestos_mayores_1950(self)-> str:
        impuestos = ""
        if self.__cantidad_de_ambientes > 1 and self.__cantidad_de_ambientes < 5:
            impuestos = "5%"
        else : 
            impuestos = "35%"
    
        return impuestos