import numpy as np
# Escribe una función recursiva que calcule la suma de todos los elementos en un array de NumPy.

# Implementa una función recursiva para encontrar el máximo elemento en un array de NumPy.
def maximo(vector:np.array) -> int:
    
    prim_pos = 0
    
    num_max = 0
    
    if len(vector) == 1:
        num_max = vector[prim_pos]
        if num_max < vector[prim_pos + 1]:
            num_max = vector[prim_pos + 1]
    else:
        num_max = maximo(vector[1:])
         
    return num_max

vector = np.array([1,2,3])
print(maximo(vector))
# Crea una función recursiva para calcular el producto de todos los elementos en un array de NumPy.

# Desarrolla una función recursiva para encontrar el índice del primer elemento que sea igual a un valor dado en un array de NumPy.

# Escribe una función recursiva para invertir un array de NumPy.

# Implementa una función recursiva para encontrar el mínimo elemento en un array de NumPy.

# Crea una función recursiva para calcular el promedio de todos los elementos en un array de NumPy.

# Desarrolla una función recursiva para contar la cantidad de elementos en un array de NumPy que sean mayores que un valor dado.

# Escribe una función recursiva para buscar un elemento en un array de NumPy y devolver su posición si está presente.

# Implementa una función recursiva para verificar si un array de NumPy está ordenado de manera ascendente.