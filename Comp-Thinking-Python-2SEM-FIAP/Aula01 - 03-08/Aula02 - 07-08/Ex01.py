def somar_numeros(a: float | int, b: float | int) -> float:
    """
    Realiza a soma de dois números.
    :param a: Primeiro número
    :param b: Segundo número
    :return: Soma dos números
    """
    soma = a + b
    return soma

x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))

resultado = somar_numeros(x, y)
print(f"O resultado da soma é: {resultado}")
