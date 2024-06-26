n = int(input())

if n == 0:
    print("NULO")
elif n > 0 and n % 2 == 0:
    print("POSITIVO PAR")
elif n > 0:
    print("POSITIVO IMPAR")
elif n < 0 and n % 2 == 0:
    print("NEGATIVO PAR")
elif n < 0:
    print("NEGATIVO IMPAR")