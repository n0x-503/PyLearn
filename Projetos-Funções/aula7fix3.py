def receber_numero() :
    n = int(input("Digite um número : "))
    return n

def par_ou_impar() :
    n = receber_numero()
    if n%2 == 0 :
        print(f"O número {n} é par!")
    else :
        print(f"O número {n} é ímpar!")

par_ou_impar()

