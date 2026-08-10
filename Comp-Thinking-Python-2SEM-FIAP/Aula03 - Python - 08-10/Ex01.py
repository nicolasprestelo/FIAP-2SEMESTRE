def mostrar_informacoes(nome: str, idade: int, cidade: str):
    """"Recebe 3 parametros: nome, idade, cidade
        Retorna as informações recebidas"""
    print(f"Informações: "
          f"nome: {nome}, "
          f"idade: {idade}, "
          f"cidade: {cidade}")

n = input("Informe o seu nome: ")
i = int(input("Informe a seu idade: "))
c = input("Informe a seu cidade: ")

mostrar_informacoes(n, i, c)