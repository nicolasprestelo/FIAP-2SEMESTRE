from sympy import *

x = symbols("x")

#Exemplo

f = 4 * x ** 2 + 6 * x

print( integrate(f, (x, 0, 2)) )

# 1 a)

f = 3 * x ** 2 + 2 * x

print( integrate(f, (x, 0, 2)) )

# b)

f = x - 1
print( integrate(f, (x, 1, 4)) )

# c)

f = 5*x + 2

print(integrate(f, (x, 0, 3)))

# d)

f = x**2 - 4*x + 3

print(integrate(f, (x, 0, 1)))

# e)

f = 6 - x

print(integrate(f, (x, 2, 5)))


# Exercicio 2

t = symbols('t')
p = 3*t + 2
print(integrate(p, (t, 0, 4)))


# Exercicio 3

v = 2*t + 3
print(integrate(v, (t, 2, 6)))

# Exercicio 4

f = x**2 + 2
print(integrate(f, (x, 0, 3)))

# Exercicio 5

f = - x**2 + 4
print(integrate(f, (x, 0, 2)))