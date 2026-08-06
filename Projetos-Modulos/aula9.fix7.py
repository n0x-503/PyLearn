import json



def salvar_aluno(nome, notas):
    soma = 0
    for i in notas:
        soma += i
    media = round(soma / len(notas))
    ArquivoJson = {"Nomes":nome, "Notas":notas, "Media": media}
    return json.dumps(ArquivoJson, indent=2)


def carregar_aluno(json_str):
    return json.loads(json_str)


json_str = salvar_aluno("Mario", [9, 8, 6, 7])
print("JSON gerado: ")
print(json_str)
print("Dados recuperados: ")

DadosRecuperados = carregar_aluno(json_str)


print(f"Nome: {DadosRecuperados['Nomes']}")
print(f"Média: {DadosRecuperados['Media']}")

with open("Dados.json", "w") as arquivo:
    json.dump(DadosRecuperados, arquivo, indent=2)

with open("Dados.json", "r") as arquivo:
    DadosLidos = json.load(arquivo)

print(f"Dado lido do arquivo Json: {DadosLidos['Media']}")