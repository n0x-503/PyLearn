text = input("Digite uma frase : ")
letras = 0
frases = 0
palavras = len(text.split())

for i in text :
    if i.lower() in "abcdefghijklmnopqrstuvwxyz" :
        letras +=1
    if i in ".!?" :
        frases +=1
L = (letras/palavras)*100
S = (frases/palavras)*100
index = round(0.0588 * L - 0.296 * S - 15.8)

if index >= 16 :
    print("grade 16+")
if index < 1 :
    print("before grade 1")
else :
    print(f"grade {index}")


