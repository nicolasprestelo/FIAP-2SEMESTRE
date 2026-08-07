
def soma_divisores(numero: int) -> int:
    """
    Calcula a soma dos divisores do número inserido
    :param numero: Numero inteiro
    :param contador: Contador para calcular
    :param soma: Soma dos divisores
    :return: Retorna a soma dos divisores
    """
    soma = 0
    contador = 1
    while contador <= numero:
        if numero % contador == 0:
            soma += contador
            contador += 1
        else:
            contador += 1
    return soma



numero = int(input("Digite um numero: "))
resultado_soma_divisores = (soma_divisores(numero))
print(f"A soma dos divisores desse número é: {resultado_soma_divisores}")
