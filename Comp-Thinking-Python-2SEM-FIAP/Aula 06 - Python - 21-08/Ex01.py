lista_dicionarios = []

for i in range(5):
    cpf = input("Digite o CPF: ")
    if cpf not in lista_dicionarios:
        nome = input("Digite o nome: ")
        dicionario = {"cpf": cpf, "nome": nome}
        lista_dicionarios.append(dicionario)
print(lista_dicionarios)