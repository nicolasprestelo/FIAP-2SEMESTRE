import json

with open("heroes.json", "r", encoding="utf-8") as arquivo:
    dicionario = json.load(arquivo)

lista = dicionario["members"]

for heroi in lista:
    lista_poderes = heroi["powers"]
    if "Flight" in lista_poderes:
        print("-" * 50)
        print(f"Nome: {heroi["name"]}")
        print(f"Poderes: {lista_poderes}")

