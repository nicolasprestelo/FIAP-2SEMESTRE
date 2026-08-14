def concatena(*args: str) -> str:
    """Concatena todos os valores em uma string"""
    string = ""
    for a in args:
        string += a + " "
    return string

print(concatena("Kaio", "123", "ABC"))


#SOLUCAO 2
def concatena_join(*args: str) -> str:
    """Concatena todos os valores em uma string utilizando join"""
    texto = " ".join(args)
    return texto
print(concatena_join("Kaio", "123", "ABC"))