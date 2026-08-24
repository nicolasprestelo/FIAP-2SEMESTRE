pessoas = {}

while True:
    cpf = input('Digite o CPF: ')
    if cpf in pessoas:
        break
    elif cpf == '':
        break
    lista_informacoes = []
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    cidade = input('Digite a cidade: ')
    lista_informacoes.append(nome)
    lista_informacoes.append(idade)
    lista_informacoes.append(cidade)
    pessoas[cpf] = lista_informacoes
print(pessoas)

cidade = input('Digite o nome da cidade que deseja procurar: ')
if cidade in pessoas.values():
    for palavra in pessoas[cidade]:
        if cidade in palavra:
            print(pessoas[cidade])