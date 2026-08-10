def concatenar_strings(string1:str, string2:str, separador:str=" ") -> str:
    """
    :param string1: Recebe a primeira string
    :param string2: Recebe a segunda string
    :param separador: Recebe a quantidade de espaços a ser utilizado
    :return: Retorna a mensagem concatenada
    """
    return string1 + separador + string2

string1 = input("Informe a primeiro string: ")
string2 = input("Informe a segunda string: ")
separador = input("Insira a quantidade de espaços: ")

print(concatenar_strings(string1, string2, separador))