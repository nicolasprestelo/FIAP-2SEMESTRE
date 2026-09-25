import requests

quantidade = int(input("Quantidade de usuários: "))
url = f"https://randomuser.me/api/?results={quantidade}"
resposta = requests.get(url)                    # realiza uma requisição à API

if resposta.status_code == 200:                 # 200: Código de Suceso
    dicionario = resposta.json()                # converte a resposta para uma estrutura do python
    lista = dicionario["results"]
    lista_nomes = []
    for usuario in lista:
        dados = usuario["name"]
        nome = dados['first']
        sobrenome = dados['last']
        nome_completo = nome + " " + sobrenome
        lista_nomes.append(nome_completo)       # insere os nomes na lista
    lista_nomes.sort()                          # ordena a lista
    for nome in lista_nomes:                    # exibe os nomes da lista
        print(nome)
else:
    print("Erro de Requisição")