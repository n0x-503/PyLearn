def calcular_media():
    numeros = []
    notas = int(input("Quando notas você quer calcular : "))
    for i in range(notas):
        valores = float(input(f"{i+1}. Nota : "))
        numeros.append(valores)
    return numeros
def media_notas():
    numeros = calcular_media()
    quantidade = len(numeros)
    soma = 0
    for i in numeros :
        soma += i
    media = soma / quantidade
    print(f"A media do aluno é {media}")

media_notas()



