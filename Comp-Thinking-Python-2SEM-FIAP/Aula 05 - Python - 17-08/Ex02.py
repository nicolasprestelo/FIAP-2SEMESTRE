def listaPalavras(frase:str)->list:
    """Retorna uma lista com as palavras da frase"""
    palavras = frase.split(" ")
    return palavras

frase = listaPalavras(input("Digite uma frase: "))
print(frase)