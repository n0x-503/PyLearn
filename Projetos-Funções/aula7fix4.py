def classificar_temp(temp):
    if temp < 15 :
        print("Classificacao: Frio")
    elif (temp > 15) and (temp < 25) :
        print("Classificacao: Agradavel")
    else :
        print("Classificacao: quente")

classificar_temp(27)
