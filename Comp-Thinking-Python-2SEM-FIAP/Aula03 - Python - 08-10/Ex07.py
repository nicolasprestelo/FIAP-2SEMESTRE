def lista_itens(itens:list= ["Lista Vazia"]):
    for item in itens:
        print(item)

lista = []

while True:
    item = input("Informe os itens da lista (insira SAIR pra sair): ")
    if item.lower() == "sair":
        break
    else:
        lista.append(item)

lista_itens(lista)