def homem(info):
    info = float(info)
    if info < 4.50:
        return 'Hemacias {:.2f}/mm3(Homem) = Baixo'.format(info)
    elif info >= 4.50 and info < 6.10:
        return 'Hemacias {:.2f}/mm3(Homem) = Normal'.format(info)
    elif info > 6.10:
        return 'Hemacias {:.2f}/mm3(Homem) = Alto'.format(info)

def mulher(info):
    info = float(info)
    if info < 4:
        return 'Hemacias {:.2f}/mm3(Mulher) = Baixo'.format(info)
    elif info >= 4 and info < 5.40:
        return 'Hemacias {:.2f}/mm3(Mulher) = Normal'.format(info)
    elif info > 5.40:
        return 'Hemacias {:.2f}/mm3(Mulher) = Alto'.format(info)

def kid(info):
    info = float(info)
    if info < 4.07:
        return 'Hemacias {:.2f}/mm3(Crianca) = Baixo'.format(info)
    elif info >= 4.07 and info < 5.37:
        return 'Hemacias {:.2f}/mm3(Crianca) = Normal'.format(info)
    elif info > 5.37:
        return 'Hemacias {:.2f}/mm3(Crianca) = Alto'.format(info)

def idoso(info):
    info = float(info)
    if info < 3.90:
        return 'Hemacias {:.2f}/mm3(Idoso) = Baixo'.format(info)
    elif info >= 3.90 and info < 5.36:
        return 'Hemacias {:.2f}/mm3(Idoso) = Normal'.format(info)
    elif info > 5.36:
        return 'Hemacias {:.2f}/mm3(Idoso) = Alto'.format(info)

valor = ""
while True:

    info = input()
    if info == "*":
        break

    info = info.split()
    valor = info[0]
    sigla = info[1]

    if sigla == "H":
        hi = homem(valor)
        print(hi)
    elif sigla == "M":
        hi = mulher(valor)
        print(hi)
    elif sigla == "C":
        hi = kid(valor)
        print(hi)
    elif sigla == "I":
        hi = idoso(valor)
        print(hi)