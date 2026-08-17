lista = []
lista2 = []

for i in range(5):
    lista.append(input("Digite um número: "))
tupla = tuple(lista)

for i in range(5):
    lista2.append(input("Digite um número: "))
tupla2 = tuple(lista2)

def concatenarTupla(tupla1:tuple, tupla2:tuple) -> tuple:
    """Concatena 2 tuplas"""
    return tupla1 + tupla2

print(concatenarTupla(tupla, tupla2))