class Estudantes:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

class Turma:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, alunos):
        self.alunos.append(alunos)
    def calcular_media(self):
        total = 0
        for i in self.alunos:
            total += i.nota
        return total / len(self.alunos)
turma = Turma()

turma.adicionar_aluno(Estudantes("Gabriel", 9.5))
turma.adicionar_aluno(Estudantes("José", 7.5))
turma.adicionar_aluno(Estudantes("Vitor", 5.0))
turma.adicionar_aluno(Estudantes("Gustavo", 7.5))

print(f"Turma: {len(turma.alunos)} alunos")
for i in turma.alunos:
    print(f"Aluno: {i.nome} | Nota: {i.nota}")
print(f"Media: {turma.calcular_media():.2f}")
if turma.calcular_media() > 6:
    print("A média da sala foi boa!")
else:
    print("A média da sala foi ruim!")









