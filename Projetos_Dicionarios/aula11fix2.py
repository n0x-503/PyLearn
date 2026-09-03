contador = {}

frase = input("Digite uma frase: ").lower().split()

for i in frase:
    if i in contador:
        contador[i] += 1
    else:
        contador[i] = 1

for k,v in contador.items():
    print(f"{k}: {v}")





