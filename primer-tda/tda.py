#Definiendo mi primer TDA 

class Empleado:
    def __init__(self,nombre,apellido,dni):
        self.nombre = nombre
        self.apellido = apellido
        self.verificar_dni(dni)
    
    def __srt__ (self) -> str:
        return self.nombre
    
    def __srt__ (self) -> str:
        return self.apellido
    
    def __srt__ (self) -> str:
        return self.dni
    
    def empleado_info (self):
        return f'{self.nombre} {self.apellido} {self.dni}' #Creo una funcion que me retorna los datos de mi empleado
    
    def verificar_dni (self,dni)-> Exception:
          if dni > 0 :
            self.dni = dni
          else:
              raise Exception("El dni es incorrecto")
            
    
empleado = Empleado("Matias","Mendoza",44547239)

print(empleado.empleado_info())