"""
#Tipos de Dados

# int (inteiro
idade = 35
numero = -400

# float (decimal)
altura = 1.78
numero = -5.0

#str (texto/string)
nome = "Nicolas Prestelo"
endereco = "Rua Belterra, 291"

#bool
valor = False
valor = True

# ---------------------------------------------------
# casting de dados ( conversao de dados)
# int()
valor = 3.99
valor = int(valor)
print(valor)

valor2 = 3.99
valor2 = round(valor2, 1)
print(valor2)


# float()
valor = "9.99"
valor = float(valor)
print(valor)

#STR()
valor = 349
valor = str(valor)
print(valor)

# type (retorna o tipo de dado de uma variável)
numero = 4.7
print(type(numero))

# ----------------------------------------------------

# # Operações de Entrada e saída
# numero = int(input("Digite um número: "))
# valor = float(input("Digite sua altura: "))
#
# print((f"O valor da variável é{numero:010.2f}"))

# ----------------------------------------------------

# operadores Aritméticos
# ** (potência)
# * (multiplicação)
# / (divisão)
# // (divisão inteira)
# % (mod)
# + (soma)
# - (subtração)

print(10 / 3)
print(10 // 3)
print(10 % 3)

# -----------------------------------------------------

#operadores Relacionais
# > (maior)
# < (menor)
# >= (maior ou igual)
# <= (menor ou igual)
# == (igual)
# != (diferente)

valor = 50
print(valor > 10)
print(valor < 10)
print(valor >= 10)
print(valor <= 10)
print(valor == 10)
print(valor != 10)

# ----------------------------------------------------

# Operadores Lógicos
# not
# and
# or
print(10 > 10 and 10 > 5)
print(10 > 10 or 10 > 5)
print( not 10 > 50)



# Estruturas de decisão simples (if)
numero = 20
if numero % 2 == 0:
    print("Par")

# Estruturas de decisão composta (if else)
if numero % 2 == 0:
    print("Par")
else:
    print("Impar")

# Estruturas de decisão encadeada (if elif else)
if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Zero")

# Estruturas de decisão aninhada:
if numero > 0:
    print("Positivo")
else:
    if numero < 0:
        print("Negativo")
    else:
        print("Zero")

# Estruturas de Seleção (match case)
opcao = int(input("Digite uma opcao: "))
match opcao:
    case 1:
        print("Opção 1")
    case 2:
        print("Opção 2")
    case 3:
        print("Opção 3")
    case _:
        print("Opção inválida")

# ---------------------------------------------------------------
# Estrutura de repetição While
senha = int(input("Infome a sua senha: "))
while senha != 123:
    print("Senha Incorreta")
    senha = input("Infome a sua senha: ")
print("Senha correta!")

nota = float(input("Infome uma nota (0 -10): "))
while nota < 0 or nota > 10:
    print("Nota inválida, Digite uma nota entre 0 e 10")
    nota = float(input("Infome uma nota (0 -10): "))
print(f"A sua nota é {nota}")


# --------------------------------------------------------------
# Estrutura de repetição for
for i in range(3, 20, 4):       # range(inicial, final, incremento)
    print(i)

# Exemplo: Variáveis contadoras
# Solicitar  a idade de 5 pessoas e contar com a quantidade de pessoas
# com idade superior a 40 anos

contador_idade = 0

for i in range(5):
    idade = int(input("Digite sua idade: "))
    if idade > 40:
        contador_idade += 1
print(f"{contador_idade} pessoas são maiores de 40 anos")
"""

contador = 0
while True:
    idade = int(input("Digite sua idade (digite -1 pra sair): "))
    if idade < 0:
        break
    if idade > 40:
        contador += 1
print(f"{contador} pessoas são maiores de 40 anos")

# Exemplo: Variáveis Somadoras
# Solicitar as notas de N alunos e calcular a média geral da turma

soma = 0
contador = 0
while True:
    nota = float(input("Digite sua nota(0-10): "))
    if nota < 0:
        break
    soma += nota
    contador += 1
media = soma / contador
print(f"Média: {media:.2f}")