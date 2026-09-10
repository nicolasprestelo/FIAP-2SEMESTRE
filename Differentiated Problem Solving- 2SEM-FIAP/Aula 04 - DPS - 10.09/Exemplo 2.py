from sympy import *

# Exemplo 2

x, h = symbols('x h')

f = 3 * x ** 2 + 4 * x - 5 # Função Original

print(diff(f, x))

# Exercicio 2

# A

f = 3*x + 5
print(diff(f, x))

# B

f = x ** 2 + 4 * x
print(diff(f, x))


# C

f = - 2 * x ** 2 + 6 * x - 3
print(diff(f, x))

# D

f = x ** 3 - 2 * x ** 2 + 3 * x
print(diff(f, x))

# E

f = Integer(8)
print(diff(f, x))