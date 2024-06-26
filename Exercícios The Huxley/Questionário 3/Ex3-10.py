def complexMedia(tipo, a, b, c):

    aritmetica = (a + b + c) / 3
    harmonica = 3 / ((1/a) + (1/b) + (1/c))
    geometrica = (a*b*c) ** (1/3)

    if tipo == "A":
        print("%.3f" % aritmetica)
    elif tipo == "H":
        print("%.3f" % harmonica)
    elif tipo == "G":
        print("%.3f" % geometrica)

tipo = input()
a = int(input())
b = int(input())
c = int(input())

complexMedia(tipo, a, b, c)