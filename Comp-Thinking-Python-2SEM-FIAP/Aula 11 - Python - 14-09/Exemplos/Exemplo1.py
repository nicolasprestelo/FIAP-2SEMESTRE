import json

with open("dados.json", "r", encoding="utf-8") as arquivo:
    lista = json.load(arquivo)
    print(lista)

for dicionario in lista:
    print("-" * 50)
    print(f"Nome: {dicionario['Nome']}")
    print(f"Idade: {dicionario['Idade']}")
    print(f"Profissão: {dicionario['Profissão']}")
    print(f"Salário: {dicionario['Salário']}")