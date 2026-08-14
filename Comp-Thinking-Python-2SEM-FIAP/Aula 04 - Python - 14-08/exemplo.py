"""
PARÂMETRO *ARGS

A utilização do parâmetro *args em Python permite que uma função aceite
um número variável de parâmetros posicionais.

Quando colocamos um * antes do nome do parâmetro, todos os parâmetros
são agrupados em uma tupla dentro da função.

Ao chamar a função é possível passar quantos parâmetros quiser
(inclusive nenhum).

Quando usar *args:
- Quando não sabemos quantos valores vão ser enviados pra função.
- Quando queremos que a função seja flexível na quantidade de argumentos.

Pontos importantes:
- O nome *args é uma convenção, você pode usar outro nome, mas o * é obrigatório
(pode ser usado por, por exemplo: *numeros, *valores, etc).
- Sempre que usado junto com parâmetros normais, ele vem depois dos parâmetros
posicionais obrigatórios.
"""


def somar_numeros(*args):
    print(args)  # Mostra a tupla com todos os parâmetros
    for a in args:  # percorre a tupla com os parâmetros
        print(a)
    return sum(args)  # retorna somatório da tupla


print(f"Soma: {somar_numeros()}")  # Soma: 0
print(f"Soma: {somar_numeros(1, 2, 3)}")  # Soma: 6
print(f"Soma: {somar_numeros(5, 10, 15, 20)}")  # Soma: 50
print(f"Soma: {somar_numeros(5, 10, 15, 20, 50, 300)}")  # Soma: 400

"""
RETORNO MÚLTIPLO

Retorno múltiplo ocorre quando uma função retorna mais de um valor de uma vez só.

Na prática, o Python retorna esses valores compactados como uma tupla,
e você pode desempacotar para variáveis separadas.
"""


def operacoes(a, b):
    soma = a + b
    produto = a * b
    return soma, produto  # retorna uma tupla (soma, produto)


resultado = operacoes(5, 3)
print(resultado)  # (8, 15)

resultado_soma, resultado_produto = operacoes(5, 3)
print(f"Soma: {resultado_soma}")  # 8
print(f"Produto: {resultado_produto}")  # 15
