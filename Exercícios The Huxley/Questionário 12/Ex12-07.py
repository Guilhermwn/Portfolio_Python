def SerieMiguelito(n):
    #n é o indice, na série, se n é 4, será o 4º numero na série
    #série: 3  7  8  12  13  17  18  22  23  27 ...
    if n == 0:
        return 'SEM RESPOSTA'
    elif n == 1:
        return 3
    elif n % 2 == 0:
        return SerieMiguelito(n-1) + 4

n = int(input())
print(SerieMiguelito(n))