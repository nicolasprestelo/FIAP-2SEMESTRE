with open("pares.txt", "r") as pares, open("impares.txt", "r") as impares, open("numeros.txt", "w") as numeros:
    lista = []
    for linha in pares:
        lista.append(int(linha))
    for linha in impares:
        lista.append(int(linha))
    lista.sort()
    for numero in lista:
        numeros.write(f"{numero}\n")
    print(lista)