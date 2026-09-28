matriz = [[1, 3, 6, 7, 10],
          [2, 5, 8, 9, 11],
          [5, 2, -100, 10, 23],
          [59, 1203, 20, 10, 293],
          [29, 982, 213, 987, 123]]

print()
for i in range(len(matriz)):                    # Indice das linhas
    for j in range(len(matriz[0])):             # Indice das colunas
        print(f"{matriz[i][j]:8}", end=" ")
    print()

menor = matriz[i][j]
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] < menor:
           menor = matriz[i][j]

print(f"O menor número é {menor}")