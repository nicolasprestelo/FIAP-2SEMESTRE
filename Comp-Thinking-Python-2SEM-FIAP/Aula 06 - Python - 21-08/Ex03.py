dados_alunos = {}

while True:
    lista_notas = []
    rm = input("Informe o RM do aluno: ")
    if rm == "":
        break
    for i in range(3):
        notas = float(input("Informe a nota do aluno: "))
        lista_notas.append(notas)
    dados_alunos = {"RM": rm, "notas": lista_notas}

for chave in dados_alunos.keys():
    media = sum(dados_alunos["notas"]) / len(dados_alunos["notas"])
    print(f"{chave}: {media:.2f}")