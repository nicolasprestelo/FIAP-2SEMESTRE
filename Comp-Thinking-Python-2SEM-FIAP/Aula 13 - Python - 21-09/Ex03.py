import requests

resposta = requests.get('https://dummyjson.com/recipes?limit=50')

if resposta.status_code == 200:

    dicionario = resposta.json()
    lista_receitas = dicionario['recipes']

    busca = input("Informe um ingrediente para fazer a busca: ").lower()

    for receita in lista_receitas:

        for ingrediente in receita['ingredients']:

            if busca in ingrediente.lower():

                print("-" * 50)
                print("Receita:", receita['name'])

                print("\nIngredientes:")
                for ingrediente in receita['ingredients']:
                    print(ingrediente)

                print("\nInstruções:")
                for instrucao in receita['instructions']:
                    print(instrucao)

                print("-" * 50)

else:
    print("Erro de Requisição")
