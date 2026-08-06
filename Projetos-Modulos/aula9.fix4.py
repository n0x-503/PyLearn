import random

def confrontos():
    times = ["Barcelona", "Real Madrid", "Liverpool", "Bayern de Munique", "Juventus", "PSG"]
    random.shuffle(times)
    print("=== CONFRONTOS DO CAMPEONATO ===")
    for i in range(3):
        print(f"Jogo {i+1}: {times[i]} vs {times[i+1]}")
        
confrontos()
