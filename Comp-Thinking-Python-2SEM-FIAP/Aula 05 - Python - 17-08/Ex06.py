lista = []

for i in range(10):
    lista.append(int(input("Digite um número: ")))

def separadorListas(lista:list) -> tuple:
    """Separa a lista em 2, uma com pares e outra com impares."""
    listaPares = []
    listaImpares = []
    for i in lista:
        if i % 2 == 0:
            listaPares.append(i)
        else:
            listaImpares.append(i)
    return listaPares, listaImpares

print(separadorListas(lista))