palavra = input("Digite uma palavra : ").lower().strip()
palavra_invertida = palavra[::-1]

if palavra == palavra_invertida :
    print("Seu palavra é um palindromo!")
else :
    print("Sua palavra não palindromo!")
