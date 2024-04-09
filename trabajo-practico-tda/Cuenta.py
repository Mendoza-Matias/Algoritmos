from Validar import validar_tipo

class Cuenta:
    def __init__(self,numero_de_cuenta:int,dni:int,saldo_cuenta:int,interes_anual:int) -> None:
        self.__numero_de_cuenta = validar_numero_cuenta(numero_de_cuenta)
        self.__dni = validar_dni(dni)
        self.__saldo_cuenta = validar_saldo(saldo_cuenta)
        self.__interes_anual = interes_anual
        
    
     #metodo __repr__
    def __repr__(self) -> str:
         return f'Cuenta Nro : {self.__numero_de_cuenta} - Titular : {self.__dni} {self.__saldo_cuenta} '
    
    #metodo para ingresar dinero
    def ingresar_dinero(self,dinero:int):
        if validar_tipo(dinero,int) and dinero > 0 :
            self.__saldo_cuenta +=  dinero
        else:
            raise Exception("El dinero no ingreso")
    
    
    def actualizar_dinero(self,dinero:int):
        if validar_tipo(dinero,int) and dinero > 0:
            self.__saldo_cuenta = dinero * self.__interes_anual // 365
    
    #metodo para retirar dinero
    def retirar_dinero(self,dinero_a_retirar:int):
        if validar_tipo(dinero_a_retirar,int) and self.__saldo_cuenta > 0:
            self.__saldo_cuenta -= dinero_a_retirar
        else:
            raise Exception("Estas seco")
    



#Validaciones----

 #validacion del dni
def validar_dni(dni:int)-> int:
        dni_ = 0
        if validar_tipo(dni,int) :
            dni_ = dni
        else :
            raise Exception("El dni no es valido")
        return dni_
    
     #validacion del saldo
def validar_saldo(saldo:int) -> float:
        saldo_ = 0 # saldo a retornar
        if validar_tipo(saldo,int) and saldo >= 0:
            saldo_ = saldo
        else:
            raise Exception("El saldo no es valido")
        return saldo_
    
     #validacion del numero de cuenta
def validar_numero_cuenta(numero_de_cuenta:int)-> int:
        num_c = 0
        if validar_tipo(numero_de_cuenta,int):
            num_c = numero_de_cuenta
        else:
            raise Exception("El numero de cuenta no es valido")

        return num_c
    

        
    