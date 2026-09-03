estoque = {
    'Macarrao':30,
    'Arroz':50,
    'Feijao':10
}


def adicionar(estoque, produto, qtq):
    for produto in estoque:
        if produto in estoque:
            estoque[produto] += qtq
        else :
            estoque[produto] = qtq

def remover(estoque, produto, qtd):
    try:
        if estoque[produto] < qtd:
            return (f"Estoque insuficiente de {produto}!")
        estoque[produto] -= qtd
    except KeyError:
        print(f"Item ({produto}) não encontrado!")

print(f"{remover(estoque, "Arroz", 100)}")
