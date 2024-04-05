# ### **Ejercicio 19**

# Las y los alumnas y alumnos de un curso se han dividido en dos grupos A y B de acuerdo al género y el nombre. El grupo A esta formado por las personas de genero femenino con una inicial de nombre anterior a la M y las personas de genero masculino con un inicial de nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte la inicial y el género, y muestre por pantalla el grupo que corresponde.

inicial = input("Ingrese la inicial del nombre")
genero = input("Ingrese el genero - M o F")

# #Grupo A esta definido F y inicial anterior < M y inicial > N
# #Grupo B esta definido M y inicial anterior

if genero == 'F' and inicial < 'M' or genero == 'M' and inicial > 'N':
    print("Grupo A")
else:
    print("Grupo B")
    
### **Ejercicio 25**
#  Escribir un programa que pida un número entero y 
#  muestre por pantalla un triángulo rectángulo 
#  como el de más abajo, de altura igual al número introducido. 
#  Por ejemplo, si el usuario ingresa el numero 4:  
#  *
#  **
#  ***
#  ****

number = int(input("Ingresa un numero"))

for i in range(number+1):
   print("*"*i)

#------------------------------------------------------------------------------------------------------

### **Ejercicio 28**
# Escribir un programa que pida un número natural **N** e imprima por pantalla la suma de los números naturales de 1 hasta **N**.

# Por ejemplo para **N = 5**, la salida debe ser:

# 1 + 2 + 3 + 4 + 5 = 15
   
count = 1;
two_number = int(input("Ingresa un numero"))
response = 0

while(count < two_number+1):
    response += count
    count+=1

print(response)

#------------------------------------------------------------------------------------------------------

#  **Ejercicio 29**

# Construir un programa que lea un número natural **N** y calcule la suma de los primeros **N** números pares.
# -  Si N = 2 -> Resultado = 2 + 4 = 6
# -  Si N = 3 -> Resultado = 2 + 4 + 6 = 12
# -  Si N = 4 -> Resultado = 2 + 4 + 6 + 8 = 20
# -  ......
# -  Para cualquier N -> Resultado = 2 + 4 + 6 +....+ 2*N

three_number = int(input("Ingrese un numero"))
two_response = 0

for indice in range(1,three_number*2 + 1):
    if(indice % 2 == 0):
        two_response += indice

print(two_response)

#------------------------------------------------------------------------------------------------------

# **Ejercicio 27**
# Escribir un programa que pida un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
# Si el usuario ingresa el numero 5:

# 1             

# 3 1           

# 5 3 1         

# 7 5 3 1       

# 9 7 5 3 1 

fourt_number = int(input("Ingresa un numero"))

for indice in range(1,fourt_number+1): #Si mi fourt_number = 6 indice = 6
    for column in reversed(range(1,2*indice,2)): #Paso ese valor y lo multiplico 6*2 = 1 3 5 7 9 11 (salto de impares)
        print(str(column),end=" ")
    print("")


N = 5
linea = ''

for i in range(1,2*N,2):
    linea = str(i) + " " + linea
    print(linea)

#------------------------------------------------------------------------------------------------------

# **Ejercicio 26**

# Escribir un programa que imprima por pantalla todas las fichas del domino, una por línea, sin repetir.

# 0 | 0 - 0 | 1 - 0 | 2 - 0 | 3 - 0 | 4 - 0 | 5 - 0 | 6

# 1 | 1 - 1 | 2 - 1 | 3 - 1 | 4 - 1 | 5 - 1 | 6

# 2 | 2 - 2 | 3 - 2 | 4 - 2 | 5 - 2 | 6

# 3 | 3 - 3 | 4 - 3 | 5 - 3 | 6

# 4 | 4 - 4 | 5 - 4 | 6

# 5 | 5 - 5 | 6

# 6 | 6

number = int(input("Ingrese un numero"))

for i in range(number): #segundo valor en el parentesis
    for j in range(i,number):
        print("|" + str(i) + "-" + str(j) + "|",end=" ")
    print()

#------------------------------------------------------------------------------------------------------

# **Ejercicio 31**

# Escribir un programa que pida un número entero y muestre por pantalla la cantidad de cifras de dicho número. Se debe resolver con divisiones sucesivas por 10 usando un bucle while.

#pedir un numero entero
#Contar la cantidad de divisiones sucesivas por 10
#1235//10 => resultado=123 y resto 5
#123//10 => resultado=12 y resto 3
#12//10 => resultado=1 y resto 2
#1//10 => resultado=0 y resto 1

six_number = int(input("Ingrese un numero entero"))
count = 0
resultado = 0

while count <= resultado : # count = 0  = resultado = 0
    if(resultado == 0):
        resultado = six_number // 10 # 
        print("resultado = "+str(resultado) + " resto = " + str(resultado % 10))
    resultado = resultado // 10
    print("resultado = "+str(resultado) + " resto = " + str(resultado % 10))
    count+= 1
    