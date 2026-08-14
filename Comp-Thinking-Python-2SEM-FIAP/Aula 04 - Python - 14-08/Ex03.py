import math

def maior_menor_valor(*args: int | float) -> tuple:
    """Recebe números e retorna o maior e menor valor"""
    maior = -math.inf
    menor = math.inf
    for a in args:
        if a > maior:
            maior = a
        if a < menor:
            menor = a
    return maior, menor

print(maior_menor_valor(1,2,3,4,5))