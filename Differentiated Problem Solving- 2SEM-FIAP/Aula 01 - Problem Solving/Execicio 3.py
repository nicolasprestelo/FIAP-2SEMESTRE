from sympy import *

# Exercicio 3

#t inicial = 2

#t final = (2 + delta t)

#Posição dos instantes:
t = symbols("t")
t = 2
print (t ** 2 + 4 * t)

#Velocidade Média:
print (t ** 2 + 4 * t)


# Calculando a velocidade no instante com o limite
t = symbols("t")
print( limit( (8 * t + t ** 2) / t, t, 0 ))