from Propiedad import Propiedad
from Cuenta import Cuenta
from Tiempo import Tiempo
from Cronometro import Cronometro

# p_uno = Propiedad("Montes de Oca",4747,"Moreno",1880,5)
# p_tres = Propiedad("Zarate",19,"Moreno",1955,6)
# p_dos = Propiedad("Zarate",20,"San Miguel",1890,3)

# print(p_tres.calcular_impuestos_arba())

# cuenta = Cuenta(123,44547239,0,2)

# cuenta.ingresar_dinero(1000)
# cuenta.retirar_dinero(500)
# cuenta.retirar_dinero(500)
# cuenta.retirar_dinero(500)
# print(cuenta)

# t_uno = Tiempo(14,40,59)
# t_dos = Tiempo(15,39,56)

# print(t_uno.mayor_duracion(t_dos))

tiempo_inicial = Cronometro.tiempo_inicial(14,10,20)
tiempo_final = Cronometro.tiempo_final(15,20,50)

print(Cronometro.diferencia_de_tiempo(tiempo_inicial,tiempo_final))
