dicionario = {}
vogais = "aeiou"
texto = input("Informe um texto: ").lower()

for letra in texto:
    if letra in vogais:
        if letra in dicionario:
            dicionario[letra] += 1
        else:
            dicionario[letra] = 1

print(dicionario)