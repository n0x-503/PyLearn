frase = input("Digite uma frase : ")
palavras = frase.split()
tamanho = len(palavras)

print(f"Numero de palavras: {tamanho}")
for i in range (len(palavras)) :
    print(f"{i+1}. {palavras[i].strip(",")}")


