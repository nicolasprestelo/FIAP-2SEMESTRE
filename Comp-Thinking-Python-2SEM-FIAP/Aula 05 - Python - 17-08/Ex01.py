def removerEspacos(string:str) -> str:
    """Remove os espaços em uma string"""
    string = string.replace(" ", "")
    return string

string = removerEspacos(input("Digite uma frase: "))
print(string)
