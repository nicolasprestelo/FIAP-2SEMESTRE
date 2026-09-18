import json

def carregar_dados():
    try:
        with open("dados.json", "r", encoding="utf-8") as dados:
            return json.loads(dados.read())
    except FileNotFoundError:
        return {}

def menu():
    print("\n")
    print("-" * 50)
    print("SISTEMA CRUD PARA CADASTRO DE PETS")
    print("-" * 50)
    print("1 - Cadastrar Pets")
    print("2 - Excluir um Pet da lista")
    print("3 - Alterar Pets na lista")
    print("4 - Listar Pets cadastrados")
    print("5 - Sair")



def cadastrar_pets(lista):
        dicionario_pet = {}
        print(f"\nPara cadastrar informe:")
        tipo = input("Digite o tipo do pet: ")
        nome = input("Digite o nome do pet: ")
        idade = input("Digite a idade do pet: ")
        dicionario_pet = {"tipo": tipo,
                          "nome": nome,
                          "idade": int(idade)}
        lista.append(dicionario_pet)
        print("Cadastro realizado com sucesso!\n")

def excluir_pets(lista):
    contador = 0
    nome_excluir = input("\nDigite o nome do pet que você deseja excluir: ")

    for i in lista:
        if i["nome"] == nome_excluir:
            lista.remove(i)
            contador += 1
            print(f"Pet {nome_excluir} removido com sucesso!\n")

    if contador == 0:
        print(f"Nenhum pet com esse nome foi localizado.")



def alterar_pets(lista):
    contador = 0
    nome_alterar = input("\nDigite o nome do pet que deseseja alterar o cadastro: ")

    for i in lista:

        if i["nome"] == nome_alterar:
            print(f"Pet localizado, insira as informações atualizadas do pet:")
            tipo = input("\nDigite o tipo do pet: ")
            nome = input("Digite o nome do pet: ")
            idade = input("Digite a idade do pet: ")

            i['tipo'] = tipo
            i['nome'] = nome
            i['idade'] = idade

            print(f"Cadastro alterado com sucesso!\n")
            contador += 1

    if contador == 0:
        print(f"Nenhum pet com esse nome foi localizado.")

def listar(lista):
    print("\n")
    if len(lista) == 0:
        print("Nenhum pet com esse nome foi localizado.")
    else:
        for dicionario in lista:
            print("-" * 50)
            print(f"Tipo: {dicionario['tipo']}")
            print(f"Nome: {dicionario['nome']}")
            print(f"Idade: {dicionario['idade']}")

def salvar_dados(lista):
    with open("dados.json", "w", encoding="utf-8") as dados:
        json.dump(lista, dados, ensure_ascii=False, indent=4)


lista = carregar_dados()
while True:
    menu()
    opcao_escolhida = input("Digite a opção desejada: ")
    if opcao_escolhida == "1":
        cadastrar_pets(lista)
        salvar_dados(lista)

    elif opcao_escolhida == "2":
        excluir_pets(lista)
        salvar_dados(lista)

    elif opcao_escolhida == "3":
        alterar_pets(lista)
        salvar_dados(lista)

    elif opcao_escolhida == "4":
        listar(lista)

    elif opcao_escolhida == "5":
        print(f"Encerrando o programa...")
        break

    else:
        print(f"Escolha uma opção válida!")
