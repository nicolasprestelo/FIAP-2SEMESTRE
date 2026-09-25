import requests

uf = input("Informe uma UF: ")
url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios"

resposta = requests.get(url, verify=False)

if resposta.status_code == 200:             # codigo de Sucesso
    lista = resposta.json()
    if len(lista) > 0:
        for dicionario in lista:
            print(dicionario["nome"])
    else:                                   # Se a lista estiver vazia
        print("UF Inválida")
else:
    print("Erro de Requisição")

