def comprar_produto(produto: str="Produto desconhecido", quantidade: int = 1):
    """
    :param produto: Recebe o nome do produto
    :param quantidade: Recebe o quantidade
    :return: Retorna a mensagem de compra com as informações do produto
    """
    return f"Compra realizada comprado com sucesso!\nProtudo: {produto}\nQuantidade: {quantidade}"

pruduto = input("Informe o nome do pruduto: ")
quantidade = int(input("Informe a quantidade: "))

print(comprar_produto(pruduto, quantidade))