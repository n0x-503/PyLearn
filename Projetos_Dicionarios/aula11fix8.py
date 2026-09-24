import json
class Personagem:
    def __init__(self, nome, classe, nivel, hp, atk):
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.hp = hp
        self.atk = atk

    def exportar(self):
        return json.dumps(self.__dict__, indent= 2)

    @classmethod
    def importa(cls, dados):
        personagens = json.loads(dados)
        return cls(personagens['nome'], personagens['classe'], personagens['nivel'], personagens['hp'], personagens['atk'])
    def exibir(self):
        print(f"Personagem importado: Nome: {self.nome} | Classe: {self.classe} | Nível {self.nivel}")

p = Personagem("Gabriel", "Mago", 20, 1000, 100)
jsonstr = p.exportar()
p1 = Personagem.importa(jsonstr)
p1.exibir()

p = Personagem("Manuel", "Invocador", 60, 20000, 1000)
jsonstr = p.exportar()
p2 = Personagem.importa(jsonstr)
print("")
p2.exibir()




