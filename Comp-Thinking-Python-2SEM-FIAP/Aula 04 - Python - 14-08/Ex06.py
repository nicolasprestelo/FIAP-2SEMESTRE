def separar_dados(*arg: str | int | float) -> tuple:
    """Recebe strings e numeros e retorna os valores separados em listas diferentes"""
    lista_string = []
    lista_numeros = []
    for a in arg:
        if type(a) == str:
            lista_string.append(a)
        elif type(a) == int or type(a) == float:
            lista_numeros.append(a)
    return lista_string, lista_numeros

print(separar_dados(1,2,3,4,5,6,7,8,9, "Lucas","Nicolas", "Pedro"))
