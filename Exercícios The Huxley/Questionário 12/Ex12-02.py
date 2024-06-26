#concluido e correto
soma = 0 

def fatorial(n):
  if n == 0:
    return 1
  else:
    return n * fatorial(n-1)

for i in range(5):
  num = int(input())
  if num % 3 == 0:
    soma += fatorial(num)

print(soma)