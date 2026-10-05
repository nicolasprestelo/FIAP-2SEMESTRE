import random

matriz = []
for i in range(5):
    linha = []
    for j in range(5):
        while True:
            numero = random.randint(1, 25)
            if numero not in matriz and numero not in linha:
                linha.append(numero)
                break
    matriz.append(linha)

for i in range(5):
    for j in range(5):
        print(f"{matriz[i][j]:4} ", end=" ")
    print()