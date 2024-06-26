call = ''

pacote = 5
resultado = 0

contador = 0

while call != "*":
    call = int(input())

    if contador > 5:
        ultrapasse = call * 0.5
        resultado += ultrapasse

    if resultado > 50:
        resultado = resultado - (resultado * (20/100))

    contador += 1

total = pacote + resultado

print("%.2f" % total)