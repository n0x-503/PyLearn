class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def desconto(self, percentual):
        if (percentual > 0) and (percentual < 100):
            print(f"Aplicando {percentual}% de desconto...")
            self.preco -= self.preco * (percentual / 100)
        else:
            print("Desculpe não aceitamos valores menores que 0 e maiores que 100")

    def exibir(self):
        print(f"Notebook: ${self.preco:.2f}")

produto = Produto("PC", 3000)
produto.exibir()
desconto = float(input("Digite um valor entre 0 e 100: "))
produto.desconto(desconto)
produto.exibir()



