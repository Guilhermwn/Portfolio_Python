#obrigatório definir as 3 funções r, b, c
#primeira linha de entrada contém o número N

#definir função r(x, y) = (3x)² + y²
def r(x, y):
    return ((3*x)**2) + (y**2)

#definir função b(x, y) = 2(x²) + (5y)²
def b(x, y):
    return (2*(x**2)) + ((5*y)**2)

#definir função c(x, y) = -100x + y³
def c(x, y):
    return ((-100)*x) + (y**3)

N = int(input()) #número que determina a quantidade de casos do teste

contador = 0

while contador < N:
    passada = input().split()
    x = int(passada[0]) #1 <= x
    y = int(passada[1]) # 100 >= x

    rafael = r(x, y)
    beto = b(x, y)
    carlos = c(x, y)
    
    if rafael > beto and rafael > carlos:
        print("Rafael ganhou")
    
    elif beto > rafael and beto > carlos:
        print("Beto ganhou")
    
    elif carlos > beto and carlos > rafael:
        print("Carlos ganhou")

    contador += 1
