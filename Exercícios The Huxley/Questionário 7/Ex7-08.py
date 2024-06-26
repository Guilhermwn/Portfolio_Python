n1 = int(input())
n2 = int(input())


numero = 1
soma = 0

while numero < 50:

    if numero % n1 == 0 and numero % n2 == 0:
        soma += 1

    numero += 1

print(soma)











#enquanto numero menor que 50, vai repetir o conteúdo dentro
#se o resto de numero dividido po n1 for igual a 0 e o resto de numero dividido por n2 for igual a 0
#soma vai somar 1
# então, enquanto o resto de numero dividido por n1 e n2 for igual a 0, vai ser adicionado um numero a soma
#cada vez que a condição for verdadeira, soma += 1
