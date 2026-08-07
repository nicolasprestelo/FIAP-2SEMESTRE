def calcular_salario (salario: float) -> float:
    """
    Calcula o reajuste salarial
    :param salario: Valor do seu salario
    :return: O valor do seu salario reajustado
    """
    if salario > 2000:
        return salario * 1.07
    else:
        return salario * 1.15

salario = float(input("Digite o valor do seu salario: "))

salario_reajustado = calcular_salario(salario)
print(f"O seu salário com o reajuste foi de: {salario} para: {salario_reajustado:.2f}")