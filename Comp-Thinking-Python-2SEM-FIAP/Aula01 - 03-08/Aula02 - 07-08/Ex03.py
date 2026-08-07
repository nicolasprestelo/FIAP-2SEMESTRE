from Ex02 import quadrado

def soma_dos_quadrados(a: int, b: int) -> int:
    """
    Calcula a soma de dois números elevados ao quadrado
    :param a: Primeiro valor
    :param b: Segundo valor
    :return: Soma dos dois valores ao quadrado
    """
    return quadrado(a) + quadrado(b)

x = float(input("Digite o primeiro valor: "))
y = float(input("Digite o segundo valor: "))

resultado = soma_dos_quadrados(x, y)
print(f"A soma dos quadrados desses números é: {resultado}")