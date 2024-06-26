from multiprocessing.sharedctypes import Value
from random import randint 
jogadores = {
    'jogador1': randint(1,6),
    'jogador2': randint(1,6),
    'jogador3': randint(1,6),
    'jogador4': randint(1,6)
}

ranking = list()

for i in jogadores.items():
    ranking.append(i)

print(ranking)
print(sorted(jogadores, key=jogadores.get))