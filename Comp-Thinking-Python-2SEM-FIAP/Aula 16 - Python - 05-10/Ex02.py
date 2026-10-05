matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        numero = int(input("Digite um número: "))
        linha.append(numero)
    matriz.append(linha)

transposta = []

for i in range(4):
    linha = []
    for j in range(4):
        linha.append(matriz[j][i])
    transposta.append(linha)

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(f"{matriz[i][j]:4} ", end=" ")
    print()

print()

for i in range(len(transposta)):
    for j in range(len(transposta[0])):
        print(f"{transposta[i][j]:4} ", end=" ")
    print()