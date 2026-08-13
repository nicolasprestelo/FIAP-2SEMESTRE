from sympy import *
import sympy as sp


# Exemplo 1
x = symbols('x')

print(limit((sqrt(x+6) -3) / (x -3), x, 3))

# Exercicio 1

print(limit((sqrt(x + 6) - 3) / (x ** 2 - 4 * x + 3), x, 3))

print(limit((sqrt(2 - x) -2) / (x ** 2 - 4), x, -2))

print(limit((x ** 3 + 27) / (sqrt(x + 9) - 3), x, 0))

print(limit((sqrt(x + 3) - 2) / (sqrt(2 * x + 2) - 2), x, 1))

print(limit((x ** 2 - 16) / (sqrt(x + 5) - 1), x, -4))


#Exemplo 2
x = symbols('x')

f_esq = x+2
f_dir = 2*x
print("Esquerda:", sp.limit(f_esq, x, 1, dir="-"))
print("Direita:", sp.limit(f_dir, x, 1, dir="+"))
