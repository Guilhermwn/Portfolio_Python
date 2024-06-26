# Esse programa recebe qualquer string, no caso desejado seria o nome de uma fruta, e em seguida
# exibe linha por linha, cada letra que compõe a palavra e um indice dessa letra

fruta = input()
indice = 0

while indice < len(fruta):
    letra = fruta[indice]
    print(indice, letra)
    indice += 1
