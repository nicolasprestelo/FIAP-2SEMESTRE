def calcular_area_triangulo(base:float=1, altura:float=1) -> float:
    """"Recebe a base a altura como parâmetro, tendo 1 como valor default
        Retorna o valor da Area do Triangulo"""
    return base*altura/2

base = float(input("Informe o valor da base: "))
altura = float(input("Informe o valor da altura: "))

area_triangulo = calcular_area_triangulo(base, altura)
print(f"{area_triangulo:.2f}")
