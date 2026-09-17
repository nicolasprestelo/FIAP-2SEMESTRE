# Preparando o ambiente
from sympy import *

# Resolução:
t = symbols('t')

c = 2 * t ** 2 + 3 * t

v = diff(c, t)

print(v)

print(v.subs(t, 3))