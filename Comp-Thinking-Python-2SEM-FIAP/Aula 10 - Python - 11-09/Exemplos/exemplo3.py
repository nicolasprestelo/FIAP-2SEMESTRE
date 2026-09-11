with open('cadastro.txt', "w", encoding="utf-8") as arquivo:
    arquivo.write("Exemplo de texto\n")
    arquivo.write("Outro texto\n")
    nome = input("Digite um nome: ")
    arquivo.write(f"Nome: {nome}\n")
    idade = int(input("Digite a idade: "))
    arquivo.write(f"{idade}\n")