def quadrado(num: int) -> int:
    """
    Calcula o quadrado do número inserido
    :param num: Numero inteiro
    :return: O resultado do número ao quadrado
    """
    return num ** 2


if __name__ == "__main__":
    numero = int(input("Digite um numero: "))
    resultado_quadrado = quadrado(numero)
    print(f"O resultado do número elevado ao quadrado é: {resultado_quadrado}")