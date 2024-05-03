import numpy as np #python -m pip install modulo_a_instalar

# v1 = np.zeros(10,int) Crear un array de 10 posiciones lleno de 0 
# v2 = np.array([1,2,3,4,5,6]) Crear un array con elementos  

# for i in range(len(v1)):
#     print(i) Iterar por posiciones

# for i in v1: Recorrer por los elementos
#     print(i)


# Ejercicio 1
# Escribir una función que recibe un numero entero N y le pide al usuario que ingrese N numeros. Al final, el programa debe retornar un vector contiendo los números que fueron ingresados. Tambien debe imprimir por pantalla la suma total de los valores y el promedio. Se deben hacer funciones para resolver el promedio y la suma total.

# def rellenar_vector(N:int) -> np.array:
#     vector = np.zeros(N,int)
   
#     for posicion in range(len(vector)):
#         numero_ingresado = int(input("Ingrese un numero"))
#         vector[posicion] = numero_ingresado
    
#     return vector
    
# def sumaTotal(vector:np.array) -> int :
#     total = 0
#     for elemento in vector:
#         total += elemento
        
#     return total

# def promedio(vector:np.array,)->int:
    
#     total = 0
    
#     for elemento in vector:
#         total += elemento
    
#     return total // len(vector)


# n = int(input("Ingrese cuantos numeros quieres ingresar"))

# arreglo = rellenar_vector(n)
# print(arreglo) #Retorna el vector
# print(sumaTotal(arreglo)) # Devuelve la suma 
# print(promedio(arreglo)) # Devuelve el promedio


# Punto 2 

# def invertir_vector(vector:np.array) -> np.array:
#     invertir_vector = vector.copy() 
#     return np.flip(invertir_vector)

# vector = np.array(["casa","auto","moto","perro","loro","leon","zapatilla"])
# vector_invertido = invertir_vector(vector)
# print(vector_invertido)    

# Punto 3

# def sumar_vectores(vector_uno:np.array,vector_dos:np.array)-> np.array :
    
#     vector_suma = np.zeros(len(vector_uno),int)
    
#     for i in range(len(vector_uno)):
#         resultado = vector_uno[i] + vector_dos[i]
#         vector_suma[i] = resultado
    
#     return vector_suma

# v_uno = np.array([1,4,6,7,9,10,2])
# v_dos = np.array([3,2,1,10,1,2,5])

# print(sumar_vectores(v_uno,v_dos))

# Punto 4

# NO ACORDE
# def desplazar_vector(vector:np.array)-> np.array:
    
#     vector_desplazado = np.zeros(0,int)
    
#     for i in range(len(vector)):
#         if i == len(vector) -1:
#             ultimo_elemento = (vector[i])
#             vector_desplazado = np.insert(vector[0:len(vector)-1],0,ultimo_elemento)
       
#     return vector_desplazado

#Esta forma es mas simple
# def desplazar_a_la_derecha(vector:np.array) -> None:
    
#     utlimo = vector[len(vector) - 1]
    
#     #Si lo dejo normal va a ir desde el 0 al largo -1
#     for posicion in reversed(range(0,len(vector)-1)):
#         vector[posicion + 1] =  vector[posicion] # En la posicion 5 le pongo el elemento de la posicion 4
        
#     vector[0] =  utlimo
        
# #Los cambios que realizo se mantienen por fuera
# v = np.array([1,2,3,4,5,9,10,21,25,78])
# desplazar_a_la_derecha(v)
# print(v)


# punto 5

# def insertar_elemento(vector:np.array,elemento_insertar:int,posicion:int)-> np.array:
#     vector_con_insercion = np.insert(vector,posicion,elemento_insertar)
#     return vector_con_insercion


# v = np.array([1,2,3,5])
# elemento = 4
# pos = 3

# print(insertar_elemento(v,elemento,pos))

# Punto 6

# def eliminar_elemento(vector:np.array,posicion:int)-> np.array:
#     vector_modificado = np.delete(vector,posicion)
#     return vector_modificado

# def desplazar_izquierda(posicion:int,vector:np.array)-> np.array:
    
#     for pos in range(posicion,len(vector)-1):
#         vector[pos] =  vector[pos+1]
    
#     vector[len(vector)-1] = 0
    
# v = np.array([1,2,3,4,5])
# pos = 1
# desplazar_izquierda(pos,v)
# print(v)

#Usar la funcion del punto 5

#Punto 7 
# def eliminar_apariciones(vector:np.array,elemento:int) -> np.array :
    
#     vector_modificado = np.zeros(0,int)
    
#     for i in range(len(vector)):
#         if(vector[i] == elemento):
#             vector[i] = 0
            
#     vector_modificado = np.copy(vector)
    
#     return vector_modificado


# v = np.array([1,2,3,4,5,5,6,8,5,10,5])
# e = 10
# print(eliminar_apariciones(v,e))

# Punto 8

# v = np.array([1,3,2,5,6,4,8,9,10])
# print(v[0:4]) #Inicio 0 a la posicion -1 
# Si no pongo nada al principio arranca en 0

#PASOS DE DOS
# print(v[0:len(v):2])


# Punto 9 | - VER BIEN EL CASO BASE - |

# def suma_elementos(vector:np.array)->int:
#     sumaTotal = None
#     if len(vector) == 0:
#         sumaTotal = 0
#     else:
#         sumaTotal = vector[0] + suma_elementos(vector[1:])
    
#     return sumaTotal

# v = np.array([1,2,3,4])
# print(suma_elementos(v))

#La suma de v = v[0] + suma[v[1:0]] un vector que arranca en 1 mas el resto
#Caso base 0 cuando(len(v)) = 0

# EJERCICIO DE PARCIAL ----
# def esPrimo(numero:int)-> bool:
#     return numero % 2 == 0

# def cantidadPrimos(vector:np.array) -> int:
#     nroPrimos = None
#     if(len(vector) == 0):
#         nroPrimos = 0
#     elif(esPrimo(vector[len(vector)-1])):
#         nroPrimos = 1 + cantidadPrimos(vector[:len(vector)-1])
#     else:
#         nroPrimos = cantidadPrimos(vector[:len(vector)-1])
#     return nroPrimos

# v = np.array([1,2,3,4,5,6]) # 3
# print(cantidadPrimos(v))
#-----

#EJERCICIO 10 Busqueda binaria

# def busquedaBinaria(vector:np.array,datoBusacado:int,pos_inicial:int,pos_final:int)-> int:

# #Hace un else if 



# v = np.array([2,3,5,7,8,12,34,56])
# busquedaBinaria(v,3,1,7)

