dicionario = {}

while True:
    nome_produto = input("Digite o nome do produto: ")
    if nome_produto == "":
        break
    valor = float(input("Digite o valor do produto: "))
    dicionario[nome_produto] = valor

print(dicionario)

for chave, valor in dicionario.items():
    if valor > 50:
        print(f"{chave}: {valor}")