def quantidadePalavras(string:str)->int:
    """Retorna uma a quantidade de palavras em uma string"""
    palavras = string.split(" ")
    return len(palavras)

string = quantidadePalavras(input("Digite uma frase: "))
print(f"Existem {string} palavras essa frase")