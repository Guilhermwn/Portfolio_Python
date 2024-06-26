bola = int(input())
caixa = input().split()

a = int(caixa[0])
l = int(caixa[1])
p = int(caixa[2])

if a < bola or l < bola or p < bola:
    print("N")
else:
    print("S")