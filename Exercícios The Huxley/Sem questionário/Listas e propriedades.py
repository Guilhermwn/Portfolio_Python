# um teste de list comprehension com fins educativos

lista = ["normando", "paragromo", "andramidas", "oriogrnadro", "froadipar", "driopnarj", "legonamipras", "braskitaval"]
#            0            1            2              3            4             5              6              7

print(lista[2:7]) #começa do indice 2(andramidas) até o item 6(legonamipras)
print(lista[::2]) #imprime os itens da lista, pulando 2 itens(0), (0+2 = indice 2), (2+2 = indice 4), (4+2 = indice 6)
print(lista[-1:-9:-1]) #imprime da direita para a esquerda, do último ao primeiro, pulando de 1 em 1
print(lista[-1:-9:-2]) #imprime da direita para a esquerda, a partir do último, pulando 2 itens