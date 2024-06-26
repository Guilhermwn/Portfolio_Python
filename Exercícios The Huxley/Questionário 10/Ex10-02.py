numero = int(input())

valores = input().split()
valores = list(map(int, valores))

menor = min(valores)

print('Menor valor:',menor)
print('Posicao:',valores.index(menor))