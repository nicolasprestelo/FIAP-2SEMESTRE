from sympy import *

#Exemplo 1:
x, h = symbols('x h')

f = 3 * x ** 2 + 4 * x + 5  # Função Original

print( limit( (f.subs(x, x+h) - f)/h, h, 0))


# Exercício 1:

# A

f = 3 * x + 5

print( limit( (f.subs(x, x+h) - f)/h, h, 0))

# B

f = x ** 2 + 4 * x

print( limit( (f.subs(x, x+h) - f)/h, h, 0))

# C

f = - 2 * x ** 2 + 6 * x - 3

print( limit( (f.subs(x, x+h) - f)/h, h, 0))

# D

f = x ** 3 - 2 * x ** 2 + 3 * x

print( limit( (f.subs(x, x+h) - f)/h, h, 0))

# E

f = Integer(8)
 
print( limit( (f.subs(x, x+h) - f)/h, h, 0))

