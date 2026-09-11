with open('arquivo.txt', "w", encoding="utf-8") as arquivo:
    while True:
        mensagem = input("Digite uma mensagem: ")
        if mensagem == "0":
            break
        else:
            arquivo.write(mensagem)