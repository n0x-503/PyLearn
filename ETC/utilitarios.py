#biblioteca da aula 9 fix 8
def eh_primo(n):
    for i in range(2, n):
        if n%i == 0:
            return False
        else:
            return True

def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def inverter_string(s):
    invertido = s[::-1]
    return invertido

def par_impar(n):
    if n % 2 == 0:
        print("Par!")
    else:
        print("Ímpar!")

def conversor_horario(n):
    horas = n / 3600
    minutos = n % 3600 / 60
    segundos = n % 3600 % 60
    conversao = f"{int(horas):02d}:{int(minutos):02d}:{int(segundos):02d}"
    return conversao





