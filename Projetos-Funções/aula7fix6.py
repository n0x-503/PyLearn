def receber_textor():
    t = input("Digite um texto : ")
    return t
def contar_vogais():
    text = receber_textor()
    vogais = 0
    for i in text :
        if i.lower() in "aeiouêãõéèíìáàúùóò":
            vogais += 1
    print(f"O números de vogais no texto é : {vogais}")

contar_vogais()

