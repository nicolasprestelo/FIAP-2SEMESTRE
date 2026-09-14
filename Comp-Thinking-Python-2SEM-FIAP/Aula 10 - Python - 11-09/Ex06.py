with open ("notas.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        lista = linha.split(" ")
        print(lista)
        media = (float(lista[-1]) + float(lista[-2]) + float(lista[-3]) + float(lista[-4])) / 4
        nome = lista[0:-4]
        nome_completo = " ".join(nome)
        print(f"Nome: {nome_completo}\nMédia: {media}")
        print("-" * 50)