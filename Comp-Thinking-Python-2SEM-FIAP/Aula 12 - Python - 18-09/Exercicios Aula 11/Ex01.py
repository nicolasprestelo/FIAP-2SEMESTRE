import json

with open("notas.txt", "r", encoding="utf-8") as arquivo:
    dicionario = {}
    for linha in arquivo:
        lista = linha.split(",")

        media = (float(lista[2]) + float(lista[3]) + float(lista[4]) + float(lista[5]))/4

        dicionario[lista[0]] = {"nome": lista[1],
                                "média": round(media, 2),
                                "notas":[float(lista[2]),
                                                           float(lista[3]),
                                                           float(lista[4]),
                                                            float(lista[5])]}


with open("notas.json", "w", encoding="utf-8") as arquivo:
    json.dump(dicionario, arquivo, indent=4, ensure_ascii=False)