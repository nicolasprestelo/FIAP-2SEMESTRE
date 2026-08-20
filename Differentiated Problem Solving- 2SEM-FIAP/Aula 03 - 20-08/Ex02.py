from sympy import *

x = Symbol('x')



# Exemplo 3

print(limit((3 * x ** 2 + 2 * x) / (2 * x ** 2 + 9), x, oo))

# Exemplo 4
print(limit((4 * x ** 2 - x) / (2 * x ** 3 - 5), x, -oo))


#Execicio 2

print(limit(5 / x, x, oo))

print(limit(3 / x ** 2, x, -oo))

print(limit((2 * x + 1) / x, x, oo))

print(limit((4 * x - 3) / x, x, -oo))

print(limit((3 * x ** 2 + 2 * x - 1) / (x ** 2 + 5), x, oo))