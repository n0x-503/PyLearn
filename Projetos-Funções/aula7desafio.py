def obter_filmes ():
    filmes = []
    nome_filmes = 0
    quantos_filmes = int(input("Quantos filmes ? "))
    for i in range(quantos_filmes):
        nome_filmes = input(f"{i+1}. qual o nome do {i+1}° filme : ")
        filmes.append(nome_filmes)
    return filmes

def obter_notas ():
    filmes = obter_filmes()
    notas = []
    quantas_notas = len(filmes)
    for i in range(quantas_notas):
        nota = int(input(f"{i+1}. Digite a nota do filme {filmes[i]} : "))
        notas.append(nota)
    return notas

def calculo_media ():
    soma = 0
    notas = obter_notas()
    quantidade = len(notas)
    for i in notas :
        soma += i
    media = soma / quantidade
    return media

def melhor_filme ():
    maior = 0
    notas = obter_notas()
    classificacao = []
    for i in notas :
        if i > maior :
            maior = i

def avaliacao_filme ():
    nota = obter_notas()
    classificacao = []
    for i in nota:
        if i >= 9:
            classificacao.append("Obra Prima!")
        elif (i >= 7) and (i < 8.9) :
            classificacao.append("Ótimo")
        elif (i >= 5) and (i < 7):
            classificacao.append("Bom")
        else :
            classificacao.append("Ruim")
    return classificacao

def classificacao_filme():
    notas = obter_notas()
    for i in range(len(notas)) :
        index_max = i
        for j in range(i + 1, len(notas)):
            index_max = j
    temp = notas[i]
    notas[i] = notas[index_max]
    notas[index_max] = temp
    classificacao = avaliacao_filme()
    return classificacao


classificacao = classificacao_filme()
for i in range(len(classificacao)):
    print(f"{i + 1}. {classificacao[i]}")






















