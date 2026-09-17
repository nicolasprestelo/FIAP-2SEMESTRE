from sympy import *

x = Symbol('x')

# A)

A = x*(20 - x)

taxa_variacao = diff(A,x)

print(x)

# B)

x_critico = solve(taxa_variacao, x)[0]
y = 20 - x
y_critico = y.subs(x, x_critico)
print(x_critico)
print(y_critico)

# C)

area_maxima = A.subs(x, x_critico)
print(area_maxima)

# D)

print(x_critico, "m x", y_critico, "m")