import senha_utils

lote = senha_utils.gerar_lote(10, 12)
print('\n=== Lote de senhas ===')
for i in range(len(lote)):
    f = senha_utils.avaliar_senha(lote[i])
    print(f'{i+1}. {lote[i]} | {f}')
