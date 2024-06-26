cont=0
total=0
custo=0
while True:
    r= input()
    if r=='*':
        break
    else:
        duracao= int(r)
        cont+=1
        if cont<=5:
            total= cont*5
            print("%.2f" % total)
        elif cont>5:
            custo = duracao * 0.50
            if custo>50:
                custo= ((custo - custo) * (20/100))
            print('%.2f' % custo)