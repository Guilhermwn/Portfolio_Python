#concluido e correto
def superdigito(numero):
    x = [int(a) for a in str(numero)] #separar o numero

    if sum(x) == numero:
        return numero
    else:
        return superdigito(sum(x))


numero = input().split()
numero = numero[0] * int(numero[1])

print(superdigito(numero))