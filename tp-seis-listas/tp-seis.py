#LISTAS - Estructura dinamica (Puede variar en tiempo de ejecucion)
#|ES POSIBLE MEZCLAR TIPOS DE DATOS|

lista_uno = list() 

lista_uno.append(1) #Agrega al final
lista_uno.append(5)
lista_uno.insert(0,2) #Agregar al principio (index,element)

print(lista_uno)

ultimo = lista_uno.pop() #Saco el ultimo y lo guardo

# print(lista_uno) #Me deja 2,1

primero = lista_uno.pop(0) #Saco el primero (index)

print(lista_uno)

# nombre_lista = [] #Otra forma de crear una lista

print(len(lista_uno)) # Imprime 1 porque hay un solo elemento


#RECORRER - (por elemento o por indice)

for element in lista_uno:
    print(f'elemento: {element} ')


for i in range(len(lista_uno)):
    print(f'indice {i} | elemento {lista_uno[i]}')
#-----

class Pila:
    def __init__(self):
        self.__pila = []
        
