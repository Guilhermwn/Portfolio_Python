# LINK: https://www.thehuxley.com/problem/304

# == EXPLICAÇÃO DO CÓDIGO ==
# Este código efetivamente desmembra um valor em reais em notas de diferentes 
# valores (R$ 100,00, R$ 50,00, R$ 20,00, R$ 10,00, R$ 5,00, R$ 2,00 e R$ 1,00) 
# e exibe a quantidade de cada nota necessária para representar o valor original.
 




numero = int(input())
trampo = numero
cem = int(numero/100)
numero = numero - (cem*100)

cinq = int(numero/50)
numero = numero - (cinq*50)

vint = int(numero/20)
numero = numero - (vint*20)

dez = int(numero/10)
numero = numero - (dez*10)

cinc = int(numero/5)
numero = numero - (cinc*5)

dois = int(numero/2)
numero = numero - (dois*2)

um = numero

print(trampo)
print(str(cem) + " nota(s) de R$ 100,00")
print(str(cinq) + " nota(s) de R$ 50,00")
print(str(vint) + " nota(s) de R$ 20,00")
print(str(dez) + " nota(s) de R$ 10,00")
print(str(cinc) + " nota(s) de R$ 5,00")
print(str(dois) + " nota(s) de R$ 2,00")
print(str(um) + " nota(s) de R$ 1,00")
