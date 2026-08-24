funcionarios = {}


while True:
    nome = input("Digite o nome do funcionario: ")
    if nome == '':
        break
    lista = []
    horas = int(input("Digite a quantidade de horas trabalhadas: "))
    valor_hora = float(input("Digite o valor da hora trabalhada: "))
    lista.append(horas)
    lista.append(valor_hora)
    funcionarios[nome] = lista

soma = 0
for hora in funcionarios.values():
    for i in hora:
        media = hora[0] * hora[1]
    soma += media

print(f"Total folha de pagamento: {soma:.2f}")