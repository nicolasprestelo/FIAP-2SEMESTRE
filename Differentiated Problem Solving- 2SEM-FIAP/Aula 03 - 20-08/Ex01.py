from sympy import *

# Exemplo 1

x = symbols("x")
print(limit(1 / (x - 2) ** 2, x, 2))

# Exemplo 2

print(limit(-7 / (5 - x) ** 2, x, 5))



#Exercicio 1

print(limit(x + 3 / (x - 2) ** 2, x, 2))

print(limit(-(x**2 + 4) / (x + 1) ** 2, x, -1))

print(limit(x ** 2 - 1 / (x - 3) ** 2, x, 3))

print(limit(x - 5 / (x + 2) ** 4, x, -2))

print(limit(x ** 2 + 2 / (x - 1) ** 2, x, 1))
