sequencia = input().split()
ultimo = sequencia[-1]
cont = 0

for elem in sequencia:
    if elem == ultimo:
        cont += 1

print(f'O numero {ultimo} apareceu {cont} vezes')