matriz = [[1, 3, 6, 7, 10],
          [2, 5, 8, 9, 11],
          [5, 2, 7, 10, 23],
          [59, 1203, 20, 10, 293],
          [29, 982, 213, 987, 123]]

soma = 0
for i in range(5):
    soma += matriz[i][i]

print(soma)

soma = 0
for i in range(5):
   soma += matriz[i][4 - i]

print(soma)