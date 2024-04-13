from Propiedad import Propiedad
from Cuenta import Cuenta
from Tiempo import Tiempo
from Cronometro import Cronometro
from Figuras import Rectangulo,Cuadrado
from Musica import Cancion,Genero


tiempo_uno = Tiempo(12,35,45)

# print(tiempo_uno)
# print(f'Tiempo en segundos {tiempo_uno.tiempo_a_segundos()}')
# print(f'De segundos a horas {Tiempo.desde_segundos(45345)}') #Devuelve un objeto de tipo Tiempo

# crono = Cronometro(Tiempo(15,40,22),Tiempo(10,12,35))
# print(crono.tiempo_empleado()) #Realiza la resta del total de segundos de ambos tiempos y me retorna la diferencia

c = Cancion("Left 4 ever","Trippie red",Tiempo(0,3,50),Genero.RAP,10)
c_dos = Cancion("The love","Trippie red",Tiempo(0,2,58),Genero.RAP,3)

resultado = Cancion.mas_votado(c,c_dos)
print(resultado)
