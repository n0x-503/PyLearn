import os


DiretorioAtual = os.getcwd()
print(f"O diretorio atual é: {DiretorioAtual}")

listaPY = []
for i in os.listdir():
    if i.endswith(".py"):
        listaPY.append(i)
for i in listaPY:
    print(i)
tamanho = len(listaPY)
print(f"A quantidade de arquivos .py nesse diretorio é: {tamanho}")