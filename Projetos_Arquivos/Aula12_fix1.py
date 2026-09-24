with open("arquivo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Python e incrivel!\n")
    arquivo.write("Arquivos sao uteis.\n")
    arquivo.write("Fim do arquivo.")

print("Arquivo criado com sucesso.")
print("Conteudo do arquivo:")
print("")

with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
    print(arquivo.read())