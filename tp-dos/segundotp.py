# Ejercicio 1
# Escribir un procedimiento que muestre por pantalla la cadena “Hola mundo!!!” cada
# vez que se la invoque

def hello_word():
    print("Hello word")

# hello_word() #Invoco mi funcion

#----------------------------------------------------------------------------------------------

# Ejercicio 2
# Escribir un procedimiento que se le pase por parámetros una cadena <nombre> y
# muestre por pantalla: “Hola <nombre>!!!”

def escribir_nombre(nombre):
        print("Hello " + nombre )

# escribir_nombre("Matias")

#----------------------------------------------------------------------------------------------
# Ejercicio 3
# Escribir una función que calcule y retorne el factorial de un numero natural. La
# operación factorial (!)

def obtenerFactoria(numero) -> int:
    factorial = 1 #El factorial de 0 es 1
    for i in range(1,numero+1):
        factorial = factorial * i      
    return factorial

# print(obtenerFactoria(5))

#----------------------------------------------------------------------------------------------


# Ejercicio 4
# Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función
# debe recibir el importe sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la
# factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un
# 21%.


# Ejercicio 5
# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de
# un cilindro usando la primera función.



# Ejercicio 6
# Escribir una función que recibe tres numeros enteros por parámetros, calcula el
# promedio y retorna “APROBADO” si el promedio es mayor o igual a 7 o
# “DESAPROBADO” si es menor.

def promedio (nota_uno,nota_dos,nota_tres):
    promedio_total = (nota_uno + nota_dos + nota_tres) // 3
    print("APROBADO" if promedio_total >= 7 else "DESAPROBADO") #

promedio(7,7,7)


# Ejercicio 7
# Escribir una función que recibe dos números enteros mayores que 1,[ n y m, ] y retorna
# la potencia n**m


def obtener_potencia(n,m)-> int:
    if(n > 1 and m > 1):
         return pow(n,m)
    
print(str(obtener_potencia(5,3)))


# Ejercicio 8
# Escribir la función máximo, que recibe 2 numeros por parámetro y retorna el mayor.
# Luego, usando esta función, escriba un programa que pida 10 números al usuario por
# teclado y al finalizar informe el mayor por pantalla.

lista = []
for i in range (1,11):
    numeroIngresado = int(input("Ingrese 10 numeros"))
    print("numero: " + str(i))
    lista.append(numeroIngresado)

def obtenerMaximo(lista:list) -> int:
    #  return num_a if num_a > num_b else num_b 
   auxiliar = lista[0]
   for i in range(len(lista)):
      if(auxiliar < lista[i]):
         auxiliar = lista[i]
    
   return auxiliar

print(obtenerMaximo(lista))


# Ejercicio 9
# Escribir una función que dado un tiempo en horas, minutos y segundos retorne esa
# misma cantidad en segundos.

def convertir_tiempo_segundos(horas:int,minutos:int,segundo:int) -> int:
    tiempo_a_segundos = segundo + minutos*60 + horas*36000 
    return tiempo_a_segundos

print(convertir_tiempo_segundos(2,20,50))

# Ejercicio 10
# Escribir una función que dado un año, retorne verdadero si es bisiesto y falso en caso
# contrario.
# Nota: Los años bisiestos son múltiplos de 4 o de 400, pero los múltiplos de 100 no lo
# son. Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no
# es bisiesto, 2000 es bisiesto, 1900 no es bisiesto

def es_bisiesto(anio):
     return ((anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0) 

print(es_bisiesto(1900))

# Ejercicio 11
# Escribir un programa que pida dos años al usuario y escriba cuántos años bisiestos
# hay entre esas dos fechas (incluidos los dos años).

def cantidad_anios_bisiestos(anio_uno,anio_dos)-> int:
 cantidad_anios_bisiestos = 0
 for i in range(anio_uno,anio_dos+1):
    if(es_bisiesto(i)):
        print("Año bisiesto " + str(i))
        cantidad_anios_bisiestos += 1

 return cantidad_anios_bisiestos

print(cantidad_anios_bisiestos(2000,2024))


# Ejercicio 12
# Escribir una función que tome por parámetro un numero entero y retorne la suma de
# sus dígitos.

def sumar_digitos(numero:int)-> int:
    num_str = str(numero) #convierto el numero a un string para poder recorrerlo
    total = 0

    for i in range(len(num_str)): # Recorre la cadena por completo
         total += int(num_str[i]) #Ir cada indice y lo combierte a un int , lo suma y lo guarda  
  
    return total


print(sumar_digitos(505))


# Ejercicio 13
# Escribir un programa que pida números positivos al usuario. Mostrar el número cuya
# sumatoria de dígitos fue mayor y la cantidad de números cuya sumatoria de dígitos
# fue menor que 10. Utilizar una o más funciones, según sea necesario.

numeros = []
for i in range (1,6):
    numero_ingresado = int(input("Ingrese 5 numeros"))
    print("numero: " + str(i))
    numeros.append(numero_ingresado)


# Encargado de devolver el numero mas grande 
def sumatoria_de_numeros(numeros:list) -> int :
    #primero sumo el primer valor de la lista
    numero_sumatoria_mayor = sumar_digitos(numeros[0]) #10 --> 10
    
    for i in range(1,len(numeros)):
        if numero_sumatoria_mayor <  sumar_digitos(numeros[i]):
            numero_sumatoria_mayor = sumar_digitos(numeros[i])

    return numero_sumatoria_mayor 

#Encargado de devolver la cantidad de sumatorias menores a 10
def cant_sum_menores_diez(numeros:list)-> int:       
    
    num_sumatoria_menor_diez = 0

    for i in range(len(numeros)):
         if sumar_digitos(numeros[i]) < 10 :
              num_sumatoria_menor_diez += 1       

    return num_sumatoria_menor_diez 

print("Numero mayor : " 
      + str(sumatoria_de_numeros(numeros)) + "||" 
      + "Cantidad de numeros menores a diez " 
      + str(cant_sum_menores_diez(numeros)))

# Ejercicio 14
# Escribir un programa que solicita al usuario el ingreso de números primos. La lectura
# finalizará cuando ingrese un número que no sea primo. Por cada número, mostrar la
# suma de sus dígitos. Al finalizar el programa, mostrar el factorial del mayor número
# ingresado. Utilizar una o más funciones, según sea necesario

def numeros_primos(numero):
    numero = int(input("Ingrese un numero primo")) 
    suma = numero
    while numero % 2 == 0:
        numero = int(input("Ingrese un numero primo"))
        suma += numero if numero % 2 == 0 else 0  
    
    print(obtenerFactoria(suma))


numeros_primos(10)