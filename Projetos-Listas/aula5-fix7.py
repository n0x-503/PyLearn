lista = []
vip = 0
for i in range (5) :
    nome = str(input("NOME : "))
    vip = str(input("VIP? (s/n) : "))
    while vip != "s" and vip != "n" :
        vip = str(input("VIP? (s/n) : "))

    if vip == "s" :
        lista.insert(0, nome)
    else :
        lista.append(nome)


print(lista)