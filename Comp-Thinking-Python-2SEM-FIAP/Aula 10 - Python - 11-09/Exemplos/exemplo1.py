# arquivo = open("alunos.txt", "r")
# arquivo.close()  # Libera memória
# #read

with open("alunos.txt") as arquivo:         #Fecha o arquivo automaticamente
    texto = arquivo.read()
    if "Pedro" in texto:
        print("Pedro está na lista")
    print(texto)
