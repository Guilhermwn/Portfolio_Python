nApostas = int(input())
apostas = ''

apoLista = list() #lista com os numeros das apostas
for i in range(nApostas):
    apostas = list(input().split(',')) #numero de apostas que vão ser dadas
    apoLista.append(apostas)

resultado = sorted(input().split('-'))
ganhadores = 0
for i in range(nApostas):
    comparado = set(apoLista[i]) & set(resultado)
    if len(comparado) >= 6:
        ganhadores += 1
print("Total de ganhadores: ", ganhadores)