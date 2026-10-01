# Preparando o ambiente:
from sympy import *

# Exemplo 1:
x = symbols("x")

f = 3 * x ** 2 + 4 * x - 5

print(integrate(f, x))

# Ex 1

# a)

f = 3 * x + 5
print(integrate(f, x))


# b)

f = x ** 2 + 4 * x
print(integrate(f, x))


# c)

f = - 2 * x ** 2 + 6 * x - 3
print(integrate(f, x))


# d)

f = x ** 3 - 2 * x ** 2 + 3 * x
print(integrate(f, x))


# e)

f = 8
print(integrate(f, x))