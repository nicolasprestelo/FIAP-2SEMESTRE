matriz = []
for i in range(5):                  # Quantidade de Linhas
    linha = []
    for j in range(4):              # Quantidade de Colunas
        n = int(input("Número: "))
        linha.append(n)
    matriz.append(linha)

for i in range(len(matriz)):                    # Indice das linhas
    for j in range(len(matriz[0])):             # Indice das colunas
        print(f"{matriz[i][j]:8}", end=" ")
    print()

numero = int(input(f"Informe o número para busca: "))

for i in range(len(matriz)):                    # Indice das linhas
    for j in range(len(matriz[0])):             # Indice das colunas
        if numero == matriz[i][j]:
            print(f"O número {numero} foi encontrado nos indices {i}x{j}")