import random
import string


#caracteres maisculos
caracteres_maisculos = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
caracteres_minusculos = "abcdefghijklmnopqrstuvwyz"

def gerar_senha(tamanho):
    todos_os_caracteres = caracteres_maisculos + caracteres_minusculos + string.digits
    tamanho_aleatorio = random.randint(1, tamanho)
    senha = ""
    for i in range(tamanho_aleatorio):
        senha += random.choice(todos_os_caracteres)
    return senha

def avaliar_senha(senha):
    maisculo = False
    minusculo = False
    numeros = False

    for i in senha:
        if i in string.digits:
            numeros = True
        if i in caracteres_maisculos:
            maisculo = True
        if i in caracteres_minusculos:
            minusculo = True

    tipos = 0
    if maisculo:
        tipos += 1
    if minusculo:
        tipos +=1
    if numeros:
        tipos +=1

    classificacao_senha = ""

    if (len(senha) < 6) and (tipos == 1):
        return "Senha Fraca!"
    if (len(senha) <= 9) and (tipos >= 2):
        return "Senha Mediana!"
    if (len(senha) > 10) and (tipos >= 3):
        return "Senha Forte!"

def gerar_lote(quantidade, tamanho):
    vetor_senhas = []
    for i in range(quantidade):
        vetor_senhas.append(gerar_senha(tamanho))
    return vetor_senhas

