n = int(input())
numero = 1
soma = 0

while numero < n:
    if numero %3 == 0 or numero % 5 == 0:
        soma += numero
    numero += 1
print(soma)