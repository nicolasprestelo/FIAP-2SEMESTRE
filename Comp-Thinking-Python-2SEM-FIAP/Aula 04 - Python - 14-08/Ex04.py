def pares(*args: int | float) -> list:
    """Recebe números e retorna uma lista com os pares"""
    pares = []
    for a in args:
        if a % 2 == 0:
            pares.append(a)
    return pares

print(pares(1,2,3,4,5,6,7,8,9))