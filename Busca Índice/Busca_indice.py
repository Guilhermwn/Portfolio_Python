def indiceSearch(lista, num):
    indices = []
    for i in range(len(lista)):
        if lista[i] == num:
            indices.append(i)
    return indices


lista = [7, 1, 2, 7, 0, 2, 8, 7]

numero1 = int(input())

print(indiceSearch(lista, numero1))
