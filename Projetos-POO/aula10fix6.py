class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def exibir(self):
        print(f"{self.nome}: R$ {self.salario} ")

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus
    def exibir(self):
        print(f"{self.nome}: R${self.salario:.2f} + R$ {self.bonus} bonus = R$ {self.salario + self.bonus}")

funcionario = Funcionario("Gabriel", 1800)
gerente = Gerente("Carlos", 5000, 1500)
funcionario.exibir()
gerente.exibir()

