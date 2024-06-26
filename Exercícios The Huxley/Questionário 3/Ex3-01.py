a = float(input())
b = float(input())
c = float(input())

media = (a+b+c)/3
max = 0

if a > media:
    max = max + 1
if b > media:
    max = max + 1
if c > media:
    max = max + 1

print(max)