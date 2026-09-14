import json

dicionario = {"rm": "12345",
              "nome": "João Silva",
              "turma": "1ESPK",
              "notas": [10.0, 6.0, 7.8]}

with open("alunos.json", "w", encoding="utf-8") as arquivo:
    json.dump(dicionario, arquivo, indent=4, ensure_ascii=False)