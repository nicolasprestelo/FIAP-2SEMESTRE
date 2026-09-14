import json

lista = []
while True:
    rm = input("RM: ")
    if rm == "":
        break
    nome = input("NOME: ")
    n1 = float(input("NOTA 1: "))
    n2 = float(input("NOTA 2: "))
    n3 = float(input("NOTA 3: "))
    dic = {"rm": rm,
           "nome": nome,
           "notas": [n1, n2, n3]}
    lista.append(dic)

    with open("cadastro.json", "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, indent=4, ensure_ascii=False)

