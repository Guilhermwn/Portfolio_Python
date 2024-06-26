N = int(input()) #coleta quantidaade de vezes que a iteração roda

notas = list() #lista armazenando as notas
for iteração in range(N): #iteração para coletar as notas e adicionar notas a lista
    nota = int(input())
    notas.append(nota)

media = sum(notas)/len(notas) #faz a média dos numeros presentes na lista nota

dezCento = media * (10/100)

countMaior = 0
for iteration in notas:
    if iteration >= media:
        countMaior +=1

countMenor = N - countMaior

print("%.2f" % media)
print(countMaior)
print(countMenor)