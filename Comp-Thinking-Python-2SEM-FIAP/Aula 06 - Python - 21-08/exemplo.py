# #------------------------------------------------------
# #   DICIONÁRIOS
# #------------------------------------------------------
#
# # SINTAXE BÁSICA
#
# # Dicionario vazio
# dicionario = {}
#
# # Dicionario com itens
# dicionario = {"rm": "570785",
#               "Nome": "Nicolas",
#               "Idade": 18}
#
# print(dicionario)
#
# #------------------------------------------------------
# # OPERAÇÕES BÁSICAS
#
# # Consultar um item
# print(dicionario["Nome"])
#
# # Alterar um item
# dicionario["Idade"] = 58
# print(dicionario)
#
# # Inserir um item
# dicionario["Cpf"] = "013219231023"
# dicionario["Turma"] = "1ESPK"
# print(dicionario)
#
# # Remover um item
# dicionario.pop("Idade")
# print(dicionario)
#
# #------------------------------------------------------
# # VERIFICAR A EXISTENCIA DE UM ITEM
#
# # Verficar a chave
# n = input("Informe a chave: ")
# if n in dicionario:
#     print("Chave cadastrada")
# else:
#     print("Chave não cadastrada")
#
# # Verificar o valor
# n = input("Informe o valor: ")
# if n in dicionario.values():
#     print("Chave cadastrada")
# else:
#     print("Chave não cadastrada")
#
# #------------------------------------------------------
# # PREENCHER O DICIONÁRIO COM INPUT
#
#
# alunos = {}         # dicionario vazio
# matricula = input("Informe o RM do aluno: ")
# nome = input("Informe o nome do aluno: ")
# turma = input("Informe o turma do aluno: ")
# alunos["rm"] = matricula
# alunos["nome"] = nome
# alunos["turma"] = turma
# print(alunos)
#
# # Cadastrar lista de dicionários
# lista = []
# while True:
#     matricula = input("Informe o RM do aluno: ")
#     if matricula == "":
#         break
#     alunos["matricula"] = matricula
#     nome = input("Informe o nome do aluno: ")
#     turma = input("Informe o turma do aluno: ")
#     dicionario = {"rm": matricula,
#                   "nome": nome,
#                   "turma": turma}
#     lista.append(dicionario)
# print(lista)
#
# #------------------------------------------------------
# # Estruturas Aninhadas
#
# # Dicionario contendo lista
# alunos = {"rm": "123512",
#           "nome": "Lucas",
#           "notas": [10, 10, 9, 8]}
#
# # Dicionário de dicionários
# alunos = {"12345": {"nome": "Pedro", "turma": "1ESPG"},
#           "98765": {"nome": "João", "turma": "1ESPJ"},
#           "56723": {"nome": "Arthur", "turma": "1ESPW"}}
#
# print(alunos["12345"]["turma"])
# alunos["98765"]["turma"] = "1ESPK"
# print(alunos)
#
# ##------------------------------------------------------
# PERCORRER O DICIONARIO

dicionario = {"rm": "123456",
              "nome": "Lucas Oliveira",
              "idade": 19}

# Percorrer apenas as chaves
for chave in dicionario.keys():
    print(chave)

# Percorrer apenas os valores
for valor in dicionario.values():
    print(valor)

#Percorrer os itens (chave-valor)
for chave, valor in dicionario.items():
    print(f"{chave.upper()}: {valor}")