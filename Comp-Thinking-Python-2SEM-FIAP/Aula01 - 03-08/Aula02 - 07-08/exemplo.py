lista = []

def cadastrar(lista, nome) -> None:
    """Cadastra o nome de um usuário na lista."""
    lista.append(nome)
    confirmar()

def confirmar() -> None:
    """Exibe a mensagem de sucesso."""
    print("Nome cadastrado com sucesso!")

def somar_numeros(a: float | int, b: float | int) -> float:
    """
    Realiza a soma de dois números.
    :param a: Primeiro número
    :param b: Segundo número
    :return: Soma dos números
    """
    soma = a + b
    return soma

nome = input("Digite o nome do cadastro: ")
cadastrar(lista, nome)

x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))
resultado = somar_numeros(x, y)
print(resultado)
