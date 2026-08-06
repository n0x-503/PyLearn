import random

def gerar_numeros(quantidade, minimo, maximo):
    lista = []
    for i in range(quantidade):
        numero_alt = random.randint(minimo, maximo)
        lista.append(numero_alt)
    maior = lista[0]
    indice_melhor = 0

    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            indice_melhor = i

    menor = lista[0]
    indice_menor = 0

    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indice_menor = i
    print(lista)
    print(f"menor: {menor}")
    print(f"maior: {maior}")
    
gerar_numeros(10, 1, 100)
