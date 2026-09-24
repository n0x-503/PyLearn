
def informacao_arquivo(texto):
    try:
        with open(texto + ".txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            print(f"Nome do arquivo: {texto}.txt")
            print(f"Linhas: {len(linhas)}")
            palavras = "".join(linhas)
            print(f"Palavras: {len(palavras.split())}")
            caracteres = len(palavras)
            print(f"Caracteres: {caracteres}")

    except FileNotFoundError:
        print("Arquivo não encontrado!")

texto = input("Digite o nome do arquivo: ")
informacao_arquivo(texto)