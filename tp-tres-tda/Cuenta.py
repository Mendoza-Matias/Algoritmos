from Validar import validar_tipo

class Cuenta:
    def __init__(self,numero_de_cuenta:str,dni:int,saldo_cuenta:float,interes_anual:int) -> None:
        self.__numero_de_cuenta = validar_numero_cuenta(numero_de_cuenta)
        self.__dni = validar_dni(dni)
        self.__saldo_cuenta = validar_saldo(saldo_cuenta)
        self.__interes_anual = interes_anual
        
    
     #metodo __repr__
    def __repr__(self) -> str:
         return f'Cuenta Nro : {self.__numero_de_cuenta} - Titular : {self.__dni} saldo(${self.__saldo_cuenta})'
    
    #metodo para ingresar dinero
    def ingresar_dinero(self,dinero:float):
        if es_saldo_valido(dinero):
            self.__saldo_cuenta = self.__saldo_cuenta + dinero
        else:
            raise Exception("No se puede ingresar el dinero")
    
    def actualizar_dinero(self,dinero:float):
        if es_saldo_valido(dinero):
            self.__saldo_cuenta = dinero * self.__interes_anual // 365
    
    #metodo para retirar dinero
    def retirar_dinero(self,dinero_a_retirar:int):
        if validar_tipo(dinero_a_retirar,int) and self.__saldo_cuenta > 0:
            self.__saldo_cuenta = self.__saldo_cuenta - dinero_a_retirar
        else:
            raise Exception("Estas seco")
    



#Validaciones----

 #validacion del dni
 
def es_saldo_valido(dinero:float)-> bool:
    return validar_tipo(dinero,float) and dinero > 0
 
def validar_dni(dni:int)-> str:
        dni_ = ""
        if validar_tipo(dni,str) :
            dni_ = dni
        else :
            raise Exception("El dni no es valido")
        return dni_
    
     #validacion del saldo
def validar_saldo(saldo:float) -> float:
        saldo_ = 0.0 # saldo a retornar
        if validar_tipo(saldo,float) and saldo >= 0:
            saldo_ = saldo
        else:
            raise Exception("El saldo no es valido")
        return saldo_
    
     #validacion del numero de cuenta
def validar_numero_cuenta(numero_de_cuenta:str)-> str:
        num_c = ""
        if validar_tipo(numero_de_cuenta,str):
            num_c = numero_de_cuenta
        else:
            raise Exception("El numero de cuenta no es valido")

        return num_c
    

        
    