 #validación de tipo
def validar_tipo(var,tipo:type) -> bool:
    return isinstance(var,tipo)

def no_es_vacio(var)-> bool:
    return var != ""

def es_positivo(var) -> bool:
    return var >= 0

