def media(nome: str, *notas: int | float) -> int | float:
    """Recebe o nome e a quantidade de notas e retorna a média do aluno"""
    media = sum(notas) / len(notas)
    return media

print(media("Nicolas",10, 9, 8))