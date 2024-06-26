#concluido e correto
def ContaDigitosPares(numero):
    x = [int(a) for a in str(numero)] #separa o numero e coloca em uma lista
    soma = 0

    for volta in range(len(x)): #verificar quantos são par
        if x[volta] % 2 == 0:
            soma += 1
    return soma 

numero = int(input())
print(ContaDigitosPares(numero))