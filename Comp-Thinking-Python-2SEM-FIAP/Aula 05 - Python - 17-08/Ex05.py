lista = []

for i in range(10):
    lista.append(int(input("Digite um número: ")))

def numerosPares(lista:list) -> int:
    """Retorna a quantidade de números pares na lista"""
    contador = 0
    for i in lista:
        if i % 2 == 0:
            contador += 1
    return contador

def somatorioImpares(lista:list) -> int:
    """Retorna a soma dos números pares na lista"""
    soma = 0
    for i in lista:
        if i % 2 != 0:
            soma += i
    return soma

print(f"A quantidade de números pares foi de: {numerosPares(lista)}")
print(f"A soma dos números ímpares foi de: {somatorioImpares(lista)}")