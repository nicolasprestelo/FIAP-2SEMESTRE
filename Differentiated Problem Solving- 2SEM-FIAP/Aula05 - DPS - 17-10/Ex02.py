from sympy import *

x = Symbol('x')

# A)

f = x ** 2 - 6 * x + 5

taxa_variacao = diff(f, x)

x_critico = solve(taxa_variacao, x)[0]

y_critico = f.subs(x,x_critico)

print(taxa_variacao)
print(x_critico)
print(y_critico)
print("\n")


# B)

f = -x ** 2 + 8 * x - 3

taxa_variacao = diff(f, x)

x_critico = solve(taxa_variacao, x)[0]

y_critico = f.subs(x,x_critico)

print(taxa_variacao)
print(x_critico)
print(y_critico)
print("\n")

# C)

f = x ** 2 + 4 * x - 5

taxa_variacao = diff(f, x)

x_critico = solve(taxa_variacao, x)[0]

y_critico = f.subs(x,x_critico)

print(taxa_variacao)
print(x_critico)
print(y_critico)
print("\n")

# D)

f = -x ** 2 - 4 * x + 5

taxa_variacao = diff(f, x)

x_critico = solve(taxa_variacao, x)[0]

y_critico = f.subs(x,x_critico)

print(taxa_variacao)
print(x_critico)
print(y_critico)
print("\n")

# E)

f = 2 * x ** 2 - 8 * x + 3

taxa_variacao = diff(f, x)

x_critico = solve(taxa_variacao, x)[0]

y_critico = f.subs(x,x_critico)

print(taxa_variacao)
print(x_critico)
print(y_critico)
print("\n")