quantidade_palavras = {}

frase = input("Digite uma frase: ")
lista_palavras = frase.split()

for palavra in lista_palavras:
    if palavra in quantidade_palavras:
        quantidade_palavras[palavra] += 1
    else:
        quantidade_palavras[palavra] = 1

print(quantidade_palavras)