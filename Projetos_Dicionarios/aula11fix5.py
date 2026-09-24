
class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
    def exibir(self):
        print(f"{self.nome} | {self.telefone} | {self.email} ")

class Agenda:
    def __init__(self):
        self.x = {}
    def adicionar(self, contato):
        self.x[contato.nome] = contato
    def buscar(self, nome):
        if nome in self.x:
            self.x[nome].exibir()
        else:
            print(f"{nome} não foi encontrado na lista de contatos!")
    def listar(self):
        for i in self.x.values():
            i.exibir()

agenda = Agenda()
agenda.adicionar(Contato("x", "1799999991", "teste@gmail.com"))
agenda.adicionar(Contato("y", "1899653432", "teste2y@gmail.com"))
agenda.listar()


