with open('impares.txt', "w") as arquivo:
    while True:
        numero = int(input("Digite um número: "))
        if numero == 0:
            break
        elif numero % 2 == 0 :
            with open("pares.txt", "w") as arquivo:
                arquivo.write(f"{numero}\n")
        arquivo.write(f" {numero}\n")