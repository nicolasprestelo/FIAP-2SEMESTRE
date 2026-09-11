with open("Ex01.txt", "w") as arquivo:
    for i in range(10):
        numero = int(input("Digite um número: "))
        arquivo.write(f" {numero} \n")
