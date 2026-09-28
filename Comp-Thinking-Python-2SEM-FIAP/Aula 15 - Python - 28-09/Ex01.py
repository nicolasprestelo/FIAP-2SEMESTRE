matriz = []
for i in range(3):                  # Quantidade de Linhas
    linha = []
    for j in range(5):              # Quantidade de Colunas
        n = int(input("Número: "))
        linha.append(n)
    matriz.append(linha)

for i in range(len(matriz)):                    # Indice das linhas
    for j in range(len(matriz[0])):             # Indice das colunas
        print(f"{matriz[i][j]:8}", end=" ")
    print()