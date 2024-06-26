numero = float(input())

if numero >= 0 and numero <= 25.0000:
    print("Intervalo [0,25]")
elif numero > 25.0000 and numero <= 50.0000000:
    print("Intervalo (25,50]")
elif numero > 50 and numero <= 75:
    print("Intervalo (50,75]")
elif numero > 75 and numero <= 100:
    print("Intervalo (75,100]")
elif numero < 0 or numero > 100:
    print("Fora de intervalo")