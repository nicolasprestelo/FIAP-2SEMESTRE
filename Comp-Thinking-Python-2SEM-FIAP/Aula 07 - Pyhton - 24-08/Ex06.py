despesas_mensais = {}

while True:
    categoria_gasto = input("Informe o categoria do gasto: ").upper()
    if categoria_gasto == "":
        break
    valor_gasto = float(input("Informe o valor do gasto: "))
    despesas_mensais[categoria_gasto] = valor_gasto
print(despesas_mensais)

maior_gasto = 0
for categoria, gasto in despesas_mensais.items():
    if gasto > maior_gasto:
        categoria_gasto = categoria
        maior_gasto = gasto
print(f"O maior gasto foi de {categoria_gasto}, no valor de R$:{maior_gasto}")