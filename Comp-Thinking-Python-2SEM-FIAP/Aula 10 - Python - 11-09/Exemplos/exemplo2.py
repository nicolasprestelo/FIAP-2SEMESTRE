with open("dados.txt", "r", encoding="utf-8") as arquivo:
    soma = 0
    contador = 0
    for linha in arquivo:
        print(linha)
        lista = linha.split(",")
        print(lista)
        print(f"ID: {lista[0]}")
        print(f"Nome: {lista[1]}")
        print(f"Idade: {lista[2]}")
        print(f"Profissão: {lista[3]}")
        print(f"Salario: {lista[4]}")
        soma += float(lista[4])
        contador += 1

    media = soma / contador
    print(f"Média dos salários: {media}")