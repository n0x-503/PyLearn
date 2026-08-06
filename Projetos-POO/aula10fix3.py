import json
class Carrinho:
    def __init__(self):
        try:
            with open("Lista.json", "r") as arquivo:
                self.itens = json.load(arquivo)
        except FileNotFoundError:
            self.itens = []
    def adicionar_item(self, nome, preco):
        self.itens.append({"nome": nome, "preco": preco})
        self.salvar()
    def salvar(self):
        with open("Lista.json", "w") as arquivo:
            json.dump(self.itens, arquivo, indent = 2)
    def remover_item(self, nome):
        for i in self.itens:
            if i ["nome"] == nome:
                self.itens.remove(i)
                break
            else:
                print("item não encontrado!")
        self.salvar()

    def total(self):
        total = 0
        for i in self.itens:
            total += i ['preco']
        return total

    def exibir(self):
        for i in self.itens:
            print(f"{i['nome']} | ${i['preco']}")

lista_produto = Carrinho()

def menu():
    print("1.Adicionar itens")
    print("2.Remover itens")
    print("3.Total")
    print("4.Exibir")
    print("5.Sair")
    resposta = int(input(""))
    if (resposta < 1) or (resposta > 5):
        print("Digite apenas as opções exibidas!")
        menu()
    elif resposta == 1:
        nome = input("Digite o nome do item : ")
        preco = float(input("Digite o preço do item : "))
        lista_produto.adicionar_item(nome, preco)
        menu()
    elif resposta == 2:
        nome = input("Digite o nome do produto que deseja remover : ")
        lista_produto.remover_item(nome)
        menu()
    elif resposta == 3:
        print(f"O valor total do itens da lista é : {lista_produto.total():.2}")
        menu()
    elif resposta ==4:
        lista_produto.exibir()
        menu()





