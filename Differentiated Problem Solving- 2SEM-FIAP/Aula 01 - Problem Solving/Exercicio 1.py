# Preparando o ambiente:
from sympy import *

# Exemplo 01
x = symbols("x")
print( limit(3 * x ** 2 + 4 * x - 5, x, 2))

#Exercicio 1a)
x = symbols("x")
print( limit (x + 5, x , 4))

#Exercicio 1b)
x = symbols("x")
print( limit(2 * x, x, 5))

#Exercicio 1c)
x = symbols("x")
print( limit(x ** 2, x ,3))

#Exercicio 1d)
x = symbols("x")
print( limit(3 * x - 1, x ,-2))

#Exercicio 1e)
x = symbols("x")
print( limit(3 * x ** 2 + 2 * x - 1, x, 10))
