# Preparando o ambiente:

from sympy import *

# Resolução:
x = Symbol('x')

f = 3 * x ** 2 + 4 * x - 5

taxa_variacao = diff(f, x)

x_critico = solve(taxa_variacao, x)[0]

y_critico = f.subs(x,x_critico)

print(taxa_variacao)
print(x_critico)
print(y_critico)