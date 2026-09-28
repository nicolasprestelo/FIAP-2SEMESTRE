
# Matriz 3x4  (3 linhas e 4 colunas)
matriz = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],]

print(matriz)

cont = 0
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] % 2 == 0:
            cont += 1

print(f"Quantidade de Números pares: {cont}")

# qtd_linhas = int(input("Informe a quantidade de linhas da matriz: "))
# qtd_colunas = int(input("Informe a quantidade de colunas da matriz: "))
#
# matriz = []
# for i in range(qtd_linhas):                  # Quantidade de Linhas
#     linha = []
#     for j in range(qtd_colunas):              # Quantidade de Colunas
#         n = int(input("Número: "))
#         linha.append(n)
#     matriz.append(linha)


# Exibir a matriz formatada em linhas e colunas
for i in range(len(matriz)):                    # Indice das linhas
    for j in range(len(matriz[0])):             # Indice das colunas
        print(f"{matriz[i][j]:8}", end=" ")
    print()