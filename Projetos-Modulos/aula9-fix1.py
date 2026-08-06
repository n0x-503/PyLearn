import math
numero = float(input("Digite um número: "))
def calculadora():
    try:
        print(f"Raiz quadrada: {round(math.sqrt(numero), 2)}")
        print(f"Floor: {round(math.floor(numero))}")
        print(f"Ceil: {round(math.ceil(numero))}")
        print(f"Log natural: {round(math.log(numero, math.e), 2)}")
    except ValueError:
        print("Erro: operacao invalida para numeros negativos.")

calculadora()