import random

matriz = []

for i in range(7):
    linha = []
    for j in range(7):
        numero = random.randint(1, 100)
        linha.append(numero)
    matriz.append(linha)

lista = []

for i in range(7):
    maior = 0

    for j in range(7):
        if matriz[i][j] > maior:
            maior = matriz[i][j]

    lista.append(maior)

for i in range(7):
    for j in range(7):
        print(f"{matriz[i][j]:4}", end=" ")
    print()

print("\nMaiores números de cada linha:")
print(lista)
