import json
import random

SKILLS = {
    "Amaterasu": {
        "dano": 200,
        "custo_chakra": 70,
        "descrição": "Chamas das trevas que não param de queimar"
    },
    "Shidori": {
        "dano": 80,
        "custo_chakra": 40,
        "descrição": "Golpe de raios super rapido e mortal"
    },
    "Susano": {
        "dano": 600,
        "custo_chakra": 285,
        "descrição": "Armadura de um samurai antigo gigante feita inteiramente de chakra"
    },
    "Ninjutso Médico": {
        "dano": -50,
        "custo_chakra": 65,
        "descrição": "Ninjutso que cura o usuario"
    }
}


class Personagem:
    def __init__(self, nome, hp, chakra, ataque):
        self.nome = nome
        self.hp = hp
        self.chakra = chakra
        self.ataque = ataque

    def __str__(self):
        return self.nome

    def esta_vivo(self):
        return self.hp > 0

    def atacar(self, inimigo):
        dano = random.randint(self.ataque - 5, self.ataque + 5)
        critico = False
        if random.randint(0, 100) <= 15:
            dano = int(dano * 1.5)
            critico = True
        inimigo.hp -= dano
        return dano, critico

    def usar_skill(self, nome_skill, inimigo):
        if nome_skill not in SKILLS:
            raise ValueError(f"A {nome_skill} não existe!")
        skill = SKILLS[nome_skill]
        if self.chakra < skill["custo_chakra"]:
            raise ValueError(f"Você não tem chakra para usar a habilidade {nome_skill}")

        self.chakra -= skill["custo_chakra"]
        dano_skill = skill["dano"]

        if dano_skill < 0:
            self.hp -= dano_skill  # Cura (subtrai negativo)
            return dano_skill, False

        inimigo.hp -= dano_skill
        return dano_skill, False


def batalha(player1, player2):
    registro_batalha = {}
    turno = 0

    while player1.esta_vivo() and player2.esta_vivo():
        turno += 1
        registro_batalha[turno] = []

        # Filtra habilidades disponíveis com base no chakra atual
        hab_disponiveis = [nome for nome, dados in SKILLS.items() if player1.chakra >= dados["custo_chakra"]]

        # Chance de usar skill ou ataque físico
        if hab_disponiveis and random.randint(0, 1):
            habilidade = random.choice(hab_disponiveis)
            dano, _ = player1.usar_skill(habilidade, player2)

            # Print em tempo real modificado
            print(
                f"O {player1.nome} usou a skill [{habilidade}] em {player2.nome} | Dano/Cura = {dano} | {player2.nome} HP: {max(player2.hp, 0)}")

            registro_batalha[turno].append({
                "Atacante": player1.nome,
                "Atacado": player2.nome,
                "dano": dano,
                "Tipo de ataque": habilidade,  # Mudado para salvar o nome da skill usada
                "HP restante": max(player2.hp, 0)
            })
        else:
            danoatk, criticoatk = player1.atacar(player2)
            if criticoatk:
                print(
                    f"{player1.nome} acertou um crítico! Dano: {danoatk} | HP de {player2.nome}: {max(player2.hp, 0)}")
            else:
                print(f"{player1.nome} atacou! Dano: {danoatk} | HP de {player2.nome}: {max(player2.hp, 0)}")

            registro_batalha[turno].append({
                "Atacante": player1.nome,
                "Atacado": player2.nome,
                "dano": danoatk,
                "Tipo de ataque": "Ataque critico" if criticoatk else "Ataque normal",
                "HP restante": max(player2.hp, 0)
            })

        if not player2.esta_vivo():
            print(f"O {player2.nome} foi derrotado!")
            break

        # Turno do Player 2
        danoatk, criticoatk = player2.atacar(player1)
        if criticoatk:
            print(f"{player2.nome} acertou um crítico! Dano: {danoatk} | HP de {player1.nome}: {max(player1.hp, 0)}")
        else:
            print(f"{player2.nome} atacou! Dano: {danoatk} | HP de {player1.nome}: {max(player1.hp, 0)}")

        registro_batalha[turno].append({
            "Atacante": player2.nome,
            "Atacado": player1.nome,
            "dano": danoatk,
            "Tipo de ataque": "Ataque critico" if criticoatk else "Ataque normal",
            "HP restante": max(player1.hp, 0)
        })

    relatorio(registro_batalha, player1, player2)


def relatorio(registro_batalha, player1, player2):
    total_dano_player1 = 0
    total_dano_player2 = 0
    turno_critico = 0
    maior_critico = 0
    autor_critico = ""

    print("\n=== BATTLE REPORT ===")

    # Este loop serve EXCLUSIVAMENTE para listar as ações de cada turno e somar os danos
    for turno, acao in registro_batalha.items():
        for i in acao:
            print(f"Turno {turno}: {i['Atacante']} -> {i['Atacado']} | {i['dano']} dmg ({i['Tipo de ataque']}) | {i['Atacado']} HP: {i['HP restante']}")

            # Se for cura (dano negativo), não soma no contador de danos causados ao oponente
            if i['dano'] > 0:
                if i['Atacante'] == player1.nome:
                    total_dano_player1 += i['dano']
                else:
                    total_dano_player2 += i['dano']

            # Verifica se o tipo de ataque contém a palavra "critico" (independente de maiúscula/minúscula)
            if "critico" in i['Tipo de ataque'].lower() and i['dano'] > maior_critico:
                maior_critico = i['dano']
                turno_critico = turno
                autor_critico = i['Atacante']


    # CORREÇÃO: Estes prints agora ficam TOTALMENTE fora dos loops 'for'
    print("\n=== ESTATÍSTICAS FINAIS ===")
    print(f"Dano total causado por {player1.nome}: {total_dano_player1}")
    print(f"Dano total causado por {player2.nome}: {total_dano_player2}")
    if maior_critico > 0:
        print(f"Maior crítico: turno {turno_critico} ({maior_critico} de dano por {autor_critico})")



player1 = Personagem("Sasuke", 1200, 300, 24)
player2 = Personagem("Rock lee", 1250, 0, 30)

batalha(player1, player2)
