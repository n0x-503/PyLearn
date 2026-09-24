import random
class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
    def atacar(self, inimigo):
        dano = random.randint(self.ataque-5, self.ataque+5)
        inimigo.vida -= dano
        print(f"{self.nome} atacou {inimigo.nome} e causou {dano} de dano!"
              f" Vida restante de {inimigo.nome} : {inimigo.vida} ")

    def esta_vivo(self):
        return self.vida > 0


inimigo = Personagem("Dragão branco dos olhos azuis", 155, 35)
heroi = Personagem("Arthur", 150, 40)
turno = 1
while inimigo.esta_vivo and heroi.esta_vivo():
    print(f"Turno {turno}")
    turno += 1
    inimigo.atacar(heroi)
    if not heroi.esta_vivo() :
        print(f"FIM DO GAME! O {inimigo.nome} venceu a batalha!")
        break
    print("")
    print("==================================")
    print(f"Turno {turno}")
    turno += 1
    heroi.atacar(inimigo)
    if not inimigo.esta_vivo() :
        print("")
        print(f"FIM DO GAME! O {heroi.nome} venceu a batalha!")
        break
    print("")
    print("==================================")











