# Preparando o ambiente
from sympy import *

# Resolução:
t = symbols('t')

s = t**2 + 4*t # Função Original

taxa_variacao = diff(s,t)

print(taxa_variacao)

print(taxa_variacao.subs(t,2))

