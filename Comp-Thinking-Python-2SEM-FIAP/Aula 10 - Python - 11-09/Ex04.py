with open("pares.txt", "w") as pares, open("impares.txt", "w") as impares:
    while True:
        numero = int(input("Digite um número: "))

        if numero == 0:
            break
        elif numero % 2 == 0:
            pares.write(f"{numero}\n")
        else:
            impares.write(f"{numero}\n")
