valores = [34, 7, 91, 15, 62, 3, 48]
maior = valores[0]
menor = valores[0]

for i in valores :
    if i > maior :
        maior = i
    if i < menor :
        menor = i
print(maior)
print(menor)