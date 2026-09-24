def receber_nome() :
    nome = input("Digite seu nome: ")
    return nome
def personalizar_nome() :
    nome = receber_nome()
    print(f"Olá {nome} seja bem vindo")
personalizar_nome()


