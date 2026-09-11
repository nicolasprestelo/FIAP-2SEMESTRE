with open("cadastro de alunos.txt", "a", encoding="utf-8") as arquivo:     #"a"
    # Permite salvar os alunos já cadastrados e adicinar novos.
    while True:
        rm = input("Digite o RM do aluno: ")
        if rm == "":
            break
        nome = input("Digite o nome do aluno: ")
        n1 = float(input("Digite a primeira nota do aluno: "))
        n2 = float(input("Digite a segunda nota do aluno: "))
        n3 = float(input("Digite a terceira nota do aluno: "))
        arquivo.write(f"{rm}, {nome}, {n1}, {n2}, {n3}\n")


with open("cadastro de alunos.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha)