def concatenar_listas(*listas: list) -> list:
    """Recebe listas e concatena os valores em apenas uma unica lista"""
    lista = []
    for i in listas:
        lista += i
    return lista

lista_a = [1,2,3,4,5]
lista_b = [6,6,7,8,4,2]
lista_c = [10,2,2,471]

print(concatenar_listas(lista_a, lista_b, lista_c))