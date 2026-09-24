import datetime
try:
    texto_usuario = input("Digite o que aconteceu hoje no seu diário: ")

    with open("diario.txt", mode="a+", encoding="utf-8") as arquivo:
        arquivo.write(f"[{datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}] {texto_usuario}\n")

        arquivo.seek(0)
        print("=== Diario ===")
        print(arquivo.read())

except Exception as e:
    print(f"Ocorreu um erro: {e}")
