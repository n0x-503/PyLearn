nome_completo = input("Nome completo: ")
nome_maiusc = nome_completo.upper()
nome_minusc = nome_completo.lower()
palavras = nome_completo.split()
nomes = len(palavras)
primeiro = palavras[0]
ultimo = palavras[-1]
caracteres = len(nome_completo)

print(f"Maiusculo : {nome_maiusc}")
print(f"Minusculo : {nome_minusc}")
print(f"Numero de nomes {nomes}")
print(f"primeiro nome : {primeiro}")
print(f"ultimo nome : {ultimo}")
print(f"caraceres : {caracteres}")


