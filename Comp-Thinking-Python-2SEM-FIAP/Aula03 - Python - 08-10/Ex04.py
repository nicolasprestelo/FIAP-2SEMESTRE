def enviar_email(destinatario: str, assunto:str ="Sem assunto", corpo:str ="") -> str:
    """Recebe o destinatario, assunto e corpo em string e retorna formatado"""
    print(f"\n{destinatario} \n {assunto}\n - {corpo}")
    print("Email enviado com sucesso")

destinatario = input("Informe o destinatario: ")
assunto = input("Informe o assunto: ")
corpo = input("Informe o corpo: ")

enviar_email(destinatario, assunto, corpo)