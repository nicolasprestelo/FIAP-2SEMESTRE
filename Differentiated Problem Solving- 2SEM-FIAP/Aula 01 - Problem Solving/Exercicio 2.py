from sympy import *

#Exercicio 2a)
x = symbols("x")
print( limit( (x ** 2 - 3 * x) / (x ** 2 - 9), x, 3))

#Exercicio 2b)
x = symbols("x")
print( limit( (x ** 2 - x - 2) / (x - 2), x , 2))

#Exercicio 2c)
x = symbols("x")
print ( limit( (x ** 2 + 3 * x + 2) / (x ** 2 - 1), x, -1))

#Exercicio 2d)
x = symbols("x")
print ( limit( ( x ** 3 - 8) / (x - 2), x, 2))

#Exercicio 2e)
x = symbols("x")
print( limit( ( x ** 3 + 8) / (x ** 2 + x - 2), x, -2))