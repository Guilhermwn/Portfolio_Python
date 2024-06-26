# Corrigir código, código atual está incorreto
num1 = int(input())
num2 = int(input())
ope = input()

result = 0

if ope == "+":
    result = num1 + num2
    print(f'{result:,.3f}')

elif ope == "-":
    result = num1 - num2
    print(f'{result:,.3f}')

elif ope == "*":
    result = num1 * num2
    print(f'{result:,.3f}')

elif ope == "/":
    result = num1 / num2
    print(f'{result:,.3f}')

while True:
    next = (input())
    ope = input()

    if ope == "+":
        result += float(next)
        print(f'{result:,.3f}')

    elif ope == "-":
        result -= float(next)
        print(f'{result:,.3f}')

    elif ope == "*":
        result *= float(next)
        print(f'{result:,.3f}')

    elif ope == "/": 
        if result == 0 and float(next) == 0:
            print("operacao nao pode ser realizada")

        elif result != 0 and float(next) != 0:
            result /= float(next)
            print(f'{result:,.3f}')
    

    if next == "&":
        break
    elif ope == "&":
        break