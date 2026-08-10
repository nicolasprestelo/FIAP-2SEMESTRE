def soma(a:float, b:float) -> float:
    """
    :param a: Primeiro parametro
    :param b: Segundo parametro
    :return: Retorna o resultado da soma
    """
    return a + b
a = float(input("Informe o primeiro valor: "))
b = float(input("Informe o segundo valor: "))

soma = soma(a, b)
print(soma)