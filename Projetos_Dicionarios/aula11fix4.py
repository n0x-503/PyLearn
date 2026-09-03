
def media_turma(notas_alunos):
    media = {
    }

    for aluno, notas in notas_alunos.items():
        total = sum(notas)
        media[aluno] = round(total/len(notas), 2)

    return media

def melhor_aluno(media):
    melhor = None
    maior_media = 0
    for aluno, media in media.items():
        if media > maior_media:
            maior_media = media
            melhor = aluno
    return melhor, maior_media


notas = {
"Mario": [8.5, 7.0, 9.2],
"Luigi": [6.0, 5.5, 7.0],
"Peach": [9.5, 9.0, 10.0]
}

media = media_turma(notas)
for aluno, m in media.items():
    print(f"{aluno} : {m}")

melhor, maior_media = melhor_aluno(media)

print()
print("O aluno que teve a melhor media foi: ")
print(f"{melhor}")
print(f"{maior_media}")





