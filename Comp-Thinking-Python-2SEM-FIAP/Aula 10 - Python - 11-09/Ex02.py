with open('Ex01.txt', 'r') as arquivo:
    somatoria = 0
    for linha in arquivo:
        somatoria += int(linha)

print(f"A somatória é: {somatoria}")