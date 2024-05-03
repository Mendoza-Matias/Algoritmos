import numpy as np

#Crear una matriz

m1 = np.zeros((4,3),int) #4 Fila | 3 Columna

m1[0,0] = 21 #0,0 0,1 0,2

# filas,col = m1.shape # Filas y columnas (CANTIDAD)

                #Filas 3 y columnas 3
m2 = np.array([ [3,1,2],
                [2,3,1],
                [1,2,3]
               ])

# for fila in m2:
#     for elem_fila in fila:
#         print(elem_fila) #Recorre la fila

n_filas,n_cols = m2.shape

for n_fila in range(n_filas):
    print(n_fila,2[n_fila])