aposta = input()
dic = dict()

while aposta != 'FIM':
    aposta = aposta.split()
    dic[aposta[0]] = aposta[1:]
    aposta = input()

resultado = input().split('-')
acertos = dict()

for i in range(len(dic)):
    comparado = set(dic.values()) & set(resultado)
    acertos[dic.values] = len(comparado)

def ordenado(dicionario):
    dicionario = sorted(dicionario, key=dicionario.get)
    for i in range(len(dicionario)):
        print(dicionario.keys()[i], dicionario.values()[i]*'+')

ordenado(acertos)