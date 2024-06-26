entrada = input()

#pega a ENTRADA e coloca dentro da lista PEDIDOS
pedidos = list()
while True:
    if entrada != 'FIM':
        entrada = entrada.upper()
        pedidos.append(entrada)
    else:
        break
    entrada = input()

#coloca os pedidos dentro de um dicionario como chave e coloca o numero de vezes que o pedido foi feito como valor
dic = dict()
for i in pedidos:
    dic[i] = pedidos.count(i)

def ordenado(dicionario):
    for i in sorted(dicionario, key=dicionario.get, reverse=True):
        print(i, '-', dicionario[i])
        break

ordenado(dic)



