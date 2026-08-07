def media(a : int, b: int, c: int) -> float:
    media = (a + b + c) / 3
    return media

x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))
z = int(input("Digite o terceiro valor: "))

resultado_media = media(x, y, z)
print(f"A média desses números é: {resultado_media:.2f}")