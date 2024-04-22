#Evaluar que hace la funcion
#Siempre debe haber un caso base

#Factorial
def factorial(N:int)->int:
    salida = None
    if N == 0:
        salida = 1
    else:
        salida = N * factorial(N-1)
    return salida

#Suseción de fibonacci
#No es optima esta solución 
def fibo(N:int)-> int:
    salida = None
    
    if N == 1 or N == 2:
        salida = 1
    else:
        salida = fibo(N-2) + fibo (N-1)
    
    return salida


#Punto 2
def gotera(dia:int)-> int:
    agua_perdida = None
    if dia == 1:
        agua_perdida = 2
    else:
        agua_perdida = 2 + gotera(dia-1)
    
    return agua_perdida
    
print(gotera(5))

#Punto 4
def triangular(N:int)->int:
  excep = None
  if N == 1:
    excep = 1
  else:
    excep = N + triangular(N -1)
  return excep
  
print(triangular(5))

# lo que hace la función del ejercicio 4 es el resultado de la suma desde 1 hasta n  numero, por ejemplo, de  1 hasta 5 seria el resultado de 1 + 2 + 3 + 4 + 5

#Punto 5

def cantidadSeguidores(n_posteos:int)-> int:
    seguidores = None
    
    if n_posteos == 0:
        seguidores = 0
    elif 1 < n_posteos < 21:
        seguidores = 1000 + cantidadSeguidores(n_posteos - 1)
    else:
        seguidores = 500 + 2*seguidores(n_posteos-1)
    
    return seguidores

# Punto 6

def colocarBaldosas(dias:int) -> int:
    
    baldosas = 0
    
    if(dias == 1):
        
        baldosas = 100
        
    elif(dias % 2 == 0):
        
        baldosas = 2 * colocarBaldosas(dias - 1)
    
    elif(dias % 2 != 0 and dias != 1):
        
        baldosas = colocarBaldosas(dias - 1) + colocarBaldosas(dias - 2 )
    
    else:
        baldosas = colocarBaldosas(dias - 1)
       
    return baldosas
    
colocarBaldosas(4)

# Punto 7



# Punto 8


# Punto 10 //Consultar sobre este
def cucarachasEnElPiso(n_Piso:int):
    salida = 0
    
    if(n_Piso == 1):
        salida = 1
    elif(n_Piso % 2 == 0):
        salida = n_Piso * 2
    else:
        salida = cucarachasEnElPiso(n_Piso - 1) + cucarachasEnElPiso(n_Piso - 2)
    
    return salida

cucarachasEnElPiso(5)

# Punto 11 // Consultar sobre este
def repetirPalabra(palabra:str,veces:int):
    
    salida = ""
    
    if(veces == 1):
        salida = palabra
    else:
        salida = repetirPalabra(palabra,veces - 1) + palabra
    
    return salida

print(repetirPalabra(3))

#12


#13 



#Faltantes = 4