# def season(hemisferio, dia, mes):
#     if hemisferio == 0  and mes >= 6 and mes <= 9:
#         print("VERAO")
#     elif hemisferio == 0 and dia > 20 and mes >= 9 and mes <= 12:
#         print("OUTONO")
#     elif hemisferio == 0 and dia > 20 and mes >= 12 and mes <= 3:
#         print("INVERNO")
#     elif hemisferio == 0 and dia > 20 and mes >= 3 and mes <= 6:
#         print("PRIMAVERA")

#     elif hemisferio == 1 and dia > 20 and mes >= 12 and mes <= 3:
#         print("VERAO")
#     elif hemisferio == 1 and dia > 20 and mes >= 3 and mes <= 6:
#         print("OUTONO")
#     elif hemisferio == 1 and dia > 20 and mes >= 6 and mes <= 9:
#         print("INVERNO")
#     elif hemisferio == 1 and dia > 20 and mes >= 9 and mes <= 12:
#         print("PRIMAVERA")

# #
# #
# #

# hemisferio = int(input())
# dia = int(input())
# mes = int(input())

# season(hemisferio, dia, mes)


def EstacaoAno(dia, mes):
    if mes in (1, 2):
        return 'VERAO'
    elif mes == 3:
        if dia < 21:
            return 'VERAO'
        else:
            return 'OUTONO'
    elif mes in (4, 5):
        return 'OUTONO'
    elif mes == 6:
        if dia < 21:
            return 'OUTONO'
        else:
            return 'INVERNO'
    elif mes in (7, 8):
        return 'INVERNO'
    elif mes == 9:
        if dia < 21:
            return 'INVERNO'
        else:
            return 'PRIMAVERA'
    elif mes in (10, 11):
        return 'PRIMAVERA'
    elif mes == 12:
        if dia < 21:
            return 'PRIMAVERA'
        else:
            return 'VERAO'