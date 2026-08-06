numeros = []
maiores = []
print ("Digite um número para sua lista : ")
for i in range(10) :
    digite = int(input(f"{i + 1} / 10 : "))
    numeros.append(digite)
for i in numeros :
    if i > 20 :
        maiores.append(i)
print(maiores)


