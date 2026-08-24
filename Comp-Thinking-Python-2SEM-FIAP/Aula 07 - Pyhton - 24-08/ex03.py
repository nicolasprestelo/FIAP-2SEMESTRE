dados_alunos = {}

while True:
    lista_notas = []
    rm = input("Informe o RM do aluno: ")
    if rm == "":
        break
    n1 = float(input("Primeira nota: "))
    n2 = float(input("Segunda nota: "))
    n3 = float(input("Terceira nota: "))
    lista = [n1, n2, n3]
    dados_alunos[rm.upper()] = lista
print(dados_alunos)

for rm, notas in dados_alunos.items():
    media = sum(lista) / len(lista)
    print(f"RM: {rm} - Média: {media}")