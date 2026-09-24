import json
import base64

class ContaBancaria:
    def __init__(self):
        try:
            with open("dados.json", "rb") as arquivo:
                cripto = arquivo.read()
                jsondados = base64.b64decode(cripto).decode()
                self.dados = json.loads(jsondados)
        except FileNotFoundError:
            self.dados = []

    def salvar (self):
        jsondados = json.dumps(self.dados)
        cripto = base64.b64encode(jsondados.encode())
        with open("dados.json", "wb") as arquivo:
            arquivo.write(cripto)
    def depositar (self, valor, cliente):
        if valor <= 0 :
            raise ValueError("ERRO! Digite apenas depositos de acima de $0")

        for contas in self.dados:
            if contas ["nome"] == cliente:
                contas ["saldo"] += valor
                print(f"Sucesso! Adicionamos um saldo de R${valor:.2f} seu saldo total agora é : R${contas['saldo']:.2f}")
                self.salvar()
                return

        print("ERRO! Cliente não encontrado")

    def sacar (self, valor, cliente):
        if (valor < 0):
            raise ValueError ("ERRO! Digite um valor positivo para efetuar o saque")

        for contas in self.dados:
            if contas ["nome"] == cliente:
                if valor > contas ["saldo"]:
                    raise ValueError("ERRO! Saldo insuficiente")
                contas ["saldo"] -= valor
                print(f"Sacando R${valor}...")
                print(f"Saldo atual : R${contas ["saldo"]}")
                self.salvar()
                return
        print("ERRO! Cliente não encontrado")

    #adicionar, listar todos, ver saldo de cliente

    def adicionar (self):
        cliente = input("Digite o nome do cliente novo : ")
        saldo = 0
        self.dados.append({'nome': cliente, 'saldo': saldo })
        self.salvar()

    def listas (self):
        for i in self.dados:
            print(f"{i["nome"]}")

    def ver_saldo(self, cliente):
        for i in self.dados:
            if i ["nome"] == cliente:
                print(f"Cliente: {i ["nome"]} -> {i ["saldo"]:.2f}")
                return

        raise ValueError("ERRO! cliente não encontrado")


conta_bancaria = ContaBancaria()

def menu():
    print("1. depositar")
    print("2. sacar")
    print("3. adicionar")
    print("4. listar")
    print("5. ver saldo")
    print("6. sair")
    resposta = int(input(""))
    if (resposta < 1) or (resposta > 6):
        print("Digite apenas as opções exibidas!")
        menu()
    elif resposta == 1:
        cliente = input("Digite o nome do cliente : ")
        valor = float(input("Digite o valor que deseja depositar : "))
        try:
            conta_bancaria.depositar(valor, cliente)
        except ValueError as e:
            print(f"{e}")
        menu()
    elif resposta == 2:
        cliente = input("Digite o nome do cliente : ")
        valor = float(input("Digite o valor que deseja sacar : "))
        try:
            conta_bancaria.sacar(valor, cliente)
        except ValueError as e:
            print(f"{e}")
        menu()
    elif resposta == 3:
        conta_bancaria.adicionar()
        menu()
    elif resposta == 4:
        conta_bancaria.listas()
        menu()
    elif resposta == 5:
        cliente = input("Digite o nome do cliente: ")
        try:
            conta_bancaria.ver_saldo(cliente)
        except ValueError as e:
            print(f"{e}")
        menu()




menu()















