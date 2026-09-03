contatos = {
    'nome': "Gabriel",
    'telefone': "1799672345",
    'email': "exemplo@hotmail.com.br",
    'cidade': "São Paulo"
}

for k,v in contatos.items():
    print(f"{k}: {v}")

contatos["telefone"] = "1799676893"
contatos["profissão"] = "Pedreiro"

print()
print("--- Atualizado ---")
for k,v in contatos.items():
    print(f"{k}: {v}")

