def imposto(salario):
    if salario <= 2000:
        return 0
    elif salario > 2000 and salario <= 3000:
        return (salario-2000) * 0.08
    elif salario > 3000 and salario <= 4500:
        return (salario - 3000) * 0.18 + 1000*0.08
    else:
        return (salario - 4500) * 0.28 + 350

s = float(input())
i = imposto(s)

if i != 0:
    print("R$ %.2f" % i) 
else:
    print("Isento")
