import json
class Inventario:
    def __init__(self):
        try:
            with open("inventario.json", "r", encoding="utf-8") as arquivo:
                self.itens = json.load(arquivo)
        except FileNotFoundError:
            self.itens = {}

    def salvar(self):
        with open("inventario.json", "w", encoding="utf-8") as arquivo:
            json.dump(self.itens, arquivo,ensure_ascii=False, indent=2)

    def adicionar(self, item, qtd):
        if item in self.itens:
            self.itens[item] =+ qtd
        else:
            self.itens[item] = qtd
        self.salvar()
    def usar(self, item):
        try:
            self.itens[item] -= 1
            if self.itens[item] == 0:
                del self.itens[item]
                print(f"Você usou a ultima unidade do item {item}")
        except KeyError:
            print(f"{item} não está no seu inventario!")
        self.salvar()
    def exibir(self):
        for item, qtd in self.itens.items():
            print(f"{item} | {qtd}")

inv = Inventario()
inv.exibir()
