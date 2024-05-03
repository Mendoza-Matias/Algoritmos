import numpy as np


# def hayRepetido(vector:np.array)-> bool:
#   return None


def esIgual(elem_uno:int,elem_dos:int)-> bool:
    return elem_uno == elem_dos

# def hayIgual(vector:np.array)-> bool:

#     salida = None
#     prim_pos = 0
    
#     if len(vector) == 0:
#         salida = False
    
#     elif(prim_pos < len(vector) - 1 and vector[prim_pos] == vector[prim_pos + 1]):
#         salida = True
    
#     else:
#         salida = hayIgual(vector[1:])
        
#     return salida


# vector = np.array([1,3,4,8,21,30,90])
# print(hayIgual(vector))        
            

# def incluidoAux(elem:int,arra3:np.array)-> bool:
#     salida = False
#     for i in range(len(arra3)):
#         if(elem == arra3[i]):
#             salida = True
    
#     return salida

# def incluido(arra1:np.array,arra2:np.array)-> bool:
    
#     salida = None
#     prim_elemento = arra1[0]
    
#     if len(arra1) == 0:
#         salida == False
    
#     if(incluidoAux(prim_elemento,arra2)):
#         salida = True
#     else:
#         salida = incluido(arra1[1:],arra2)
    
#     return salida 



# v1 = np.array([12, 13, 14])
# v2 = np.array([2, 4, 1, 2, 7, 9])
# print(incluido(v1,v2))