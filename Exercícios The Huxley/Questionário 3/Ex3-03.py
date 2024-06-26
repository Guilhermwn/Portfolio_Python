dias = int(input())
totalkm = int(input())

maxkm = dias * 100
kmextra = totalkm - maxkm 
taxaextra = kmextra * 12

total = dias*90
tudo = total + taxaextra


if totalkm > maxkm:
    print("%.2f" % tudo)
else:
    print("%.2f" % total)