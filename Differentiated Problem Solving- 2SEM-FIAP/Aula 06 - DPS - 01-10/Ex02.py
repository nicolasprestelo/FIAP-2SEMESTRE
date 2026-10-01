# Preparando o ambiente:
from sympy import *

#Ex 1 a)

t,C = symbols('t C')

v = 2 * t + 4

s = integrate(v, t) + C
print(s)

equacao = Eq(s.subs(t, 0), 0)
valor_C = solve(equacao, C)[0]
print(valor_C)

s_final = s.subs(C, valor_C)
print(s_final)

# b )

s_2 = s_final.subs(t, 2)
print(s_2)