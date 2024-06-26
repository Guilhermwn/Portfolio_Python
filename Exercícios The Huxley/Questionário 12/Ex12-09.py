#concluido e correto
def fatorial(numero):
    if numero == 0:
        return 1
    else: 
        return numero * fatorial(numero - 1)

numeros = int(input())

while numeros != -1:
    print(fatorial(numeros))
    numeros = int(input())