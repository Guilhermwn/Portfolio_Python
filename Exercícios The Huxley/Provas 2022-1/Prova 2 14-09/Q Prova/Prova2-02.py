def corrigir_inteiro(valor):
   dado = ""
   for i in valor:
    if i == "A" or i == "a":
        dado.pop(4)
    if i == "E" or i == "e":
        dado.pop(3)
    if i == "O" or i == "o":
        dado.pop(0)
    if i == "I" or i == "i":
        dado.pop(1)
    if i == "S" or i == "s":
        dado.pop(5)
    else:
        dado.pop(i)
    return dado

valores = input().split(",")
contador = 0

for i in valores:
    a = corrigir_inteiro(valores[i])
    a = int(a)
    
    b = b + a
    contador += 1
print("%.2f" % (b/7))