import datetime

def exibir_data_hora():
    dia_atual = datetime.date.today()
    data_hora = datetime.datetime.now()
    data_hora.strftime('%d/%m/%Y %H:%M:%S')
    print(f"Data atual: {dia_atual}")

def dias_para_fim_do_ano():
    fim_ano = datetime.date(2026, 12, 31)
    dia_atual = datetime.date.today()
    dias_fimano = fim_ano - dia_atual
    print(f"Faltam {dias_fimano.days} dias para o fim do ano")

exibir_data_hora()
dias_para_fim_do_ano()
