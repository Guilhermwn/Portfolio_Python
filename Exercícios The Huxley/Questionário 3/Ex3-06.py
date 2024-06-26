a = int(input())
b = int(input())
c = int(input())
menor = 0

if a < b and a < c:
    menor = a
elif b < c:
    menor = b
else:
    menor = c

print(menor)