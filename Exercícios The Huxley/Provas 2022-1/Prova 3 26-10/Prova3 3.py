nApostas = int(input()) #precisa receber o numero em inteiro
aposta = ''

apoLista = list()
for i in range(nApostas):
    aposta = list(input().split(',')) #colocar as apostas dentro de uma lista
    apoLista.append(aposta)

resultado = sorted(input().split()) #alterado o .split('-')) para .split(''))
contador = 0
for i in range(nApostas):
    comparado = set(apoLista[i]) & set(resultado)
    if len(comparado) >= 6:
        contador += 1
print("Total de ganhadores:", contador)